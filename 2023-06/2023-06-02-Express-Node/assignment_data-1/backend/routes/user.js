var express = require('express');
var router = express.Router();
const db = require('../components/database')
const jwt = require('jsonwebtoken');

var bl = require('./var')
blacklist = bl.blacklist

/* GET user listing. */

router.post('/register', function (req, res) {
  let data = undefined;
  try {
    data = req.body;
    if (!data || !data['email'] || !data['password']) {
      throw new Error("lack of email");
    }
  } catch (err) {
    res.status(400).send({
      "error": true,
      "message": "Request body incomplete, both email and password are required"
    });
    return;
  }

  db('users').insert(data).then(function () {
    res.status(201).send({
      "message": "User created"
    })
  }).catch(function (err) {
    console.error(err);
    res.status(409).send({
      "error": true,
      "message": "User already exists"
    })
  })
});

router.post('/login', async function (req, res) {
  let data = undefined;
  try {
    data = req.body;
    if (!data || !data['email'] || !data['password']) {
      throw new Error("lack of email");
    }
  } catch (err) {
    return res.status(400).send({
      "error": true,
      "message": "Request body incomplete, both email and password are required"
    });
  }

  const email = data['email']

  const expiry = data['longExpiry'] ? data['longExpiry'] : false;
  let bearer = data['bearerExpiresInSeconds'] ? data['bearerExpiresInSeconds'] : 600;
  let refresh = data['refreshExpiresInSeconds'] ? data['refreshExpiresInSeconds'] : 86400;

  let user = await db.select('*').from('users').where('email', email).andWhere('password', data['password'])
  if (user.length != 1) {
    return res.status(401).send({
      "error": true,
      "message": "Incorrect email or password"
    })
  }

  bearer = expiry ? 365 * 24 * 3600 : bearer
  const payloadBearer = { "email": email, "expire": Date.now() + bearer * 1000 }
  const bearerToken = jwt.sign(payloadBearer, 'secret', { expiresIn: bearer })

  refresh = expiry ? 365 * 24 * 3600 : refresh
  const payloadRefresh = { "email": email, "expire": Date.now() + refresh * 1000, 'bearer': bearer, 'refresh': refresh }
  const refreshToken = jwt.sign(payloadRefresh, 'secret_refresh', { expiresIn: refresh });

  const msg = {
    "bearerToken": {
      "token": bearerToken,
      "token_type": "Bearer",
      "expires_in": bearer
    },
    "refreshToken": {
      "token": refreshToken,
      "token_type": "Refresh",
      "expires_in": refresh
    }
  }
  res.send(msg)
});

router.post('/refresh', (req, res) => {
  const refreshToken = req.body.refreshToken;
  if (!refreshToken) {
    return res.status(400).send({
      "error": true,
      "message": "Request body incomplete, refresh token required"
    });
  }

  if (blacklist.has(refreshToken)) {
    return res.status(401).send({
      "error": true,
      "message": "JWT token has expired"
    })
  }

  jwt.verify(refreshToken, 'secret_refresh', (err, payloadRefresh) => {
    if (err) {
      if (err.message == 'jwt malformed') {
        return res.status(401).send({
          "error": true,
          "message": "Invalid JWT token"
        })
      }
      return res.status(401).send({
        "error": true,
        "message": "JWT token has expired"
      })
    } 
    if (payloadRefresh['expire'] < Date.now()) {
      return res.status(401).send({
        "error": true,
        "message": "JWT token has expired"
      })
    }

    const payloadBearer = { "email": payloadRefresh['email'], "expire": Date.now() + payloadRefresh['bearer'] * 1000 }
    const bearerToken = jwt.sign(payloadBearer, 'secret', { expiresIn: payloadRefresh['bearer'] })
    payloadRefresh = {
      "email": payloadRefresh['email'], "expire": Date.now() + payloadRefresh['refresh'] * 1000,
      'bearer': payloadRefresh['bearer'], 'refresh': payloadRefresh['refresh']
    }
    const refreshToken = jwt.sign(payloadRefresh, 'secret_refresh', { expiresIn: payloadRefresh['refresh'] });

    const msg = {
      "bearerToken": {
        "token": bearerToken,
        "token_type": "Bearer",
        "expires_in": payloadRefresh['bearer']
      },
      "refreshToken": {
        "token": refreshToken,
        "token_type": "Refresh",
        "expires_in": payloadRefresh['refresh']
      }
    }
    res.send(msg)
  });
});

router.post('/logout', (req, res) => {
  const refreshToken = req.body.refreshToken;

  if (!refreshToken) {
    return res.status(400).send({
      "error": true,
      "message": "Request body incomplete, refresh token required"
    });
  }

  if (blacklist.has(refreshToken)) {
    return res.status(401).send({
      "error": true,
      "message": "JWT token has expired"
    })
  }

  jwt.verify(refreshToken, 'secret_refresh', (err, payloadRefresh) => {
    if (err) {
      if (err.message == 'jwt malformed') {
        return res.status(401).send({
          "error": true,
          "message": "Invalid JWT token"
        })
      }
      return res.status(401).send({
        "error": true,
        "message": "JWT token has expired"
      })
    } 
    if (payloadRefresh['expire'] < Date.now()) {
      return res.status(401).send({
        "error": true,
        "message": "JWT token has expired"
      })
    }

    blacklist.add(refreshToken);

    res.send({
      "error": false,
      "message": "Token successfully invalidated"
    });
  })
});

router.get('/:email/profile', async (req, res, next) => {
  const email = req.params.email;
  let token = req.headers['authorization']

  let return_unauth = async function () {
    const person = await db.select('email', 'firstName', 'lastName').from('users').where('email', email);
    if (person.length == 1) {
      return res.send(person[0]);
    }
    return res.status(404).send({
      "error": true,
      "message": "User not found"
    });
  }

  if (!token) {
    return return_unauth();
  }
  else if ((token.length <= 7) || (token.slice(0, 7) != 'Bearer ')) {
    return res.status(401).send({
      "error": true,
      "message": "Authorization header is malformed"
    })
  }
  token = token.slice(7, token.length);

  async function callback(err, bearerPayload) {
    if (err) {
      if (err.message == 'jwt expired') {
        return res.status(401).send({
          "error": true,
          "message": "JWT token has expired"
        })
      }
      return res.status(401).send({
        "error": true,
        "message": "Invalid JWT token"
      })
    }
    if (bearerPayload['expire'] < Date.now()) {
      return res.status(401).send({
        "error": true,
        "message": "JWT token has expired"
      })
    }
    if (bearerPayload['email'] == email) { // authed
      const person = await db.select('email', 'firstName', 'lastName', 'dob', 'address').from('users').where('email', email);
      if (person.length == 1) {
        return res.send(person[0]);
      }
      return res.status(404).send({
        "error": true,
        "message": "User not found"
      });
    }

    return return_unauth();
  }

  jwt.verify(token, 'secret', callback)
});

router.put('/:email/profile', (req, res) => {

  if (!req.body.firstName || !req.body.lastName || !req.body.dob || !req.body.address) {
    return res.status(400).send({
      "error": true,
      "message": "Request body incomplete: firstName, lastName, dob and address are required"
    })
  }

  const date = new Date(req.body.dob)
  if (isNaN(date)) {
    return res.status(400).send({
      "error": true,
      "message": "Invalid input: dob must be a real date in format YYYY-MM-DD"
    })
  }

  if (typeof req.body.firstName != "string" || typeof req.body.lastName != "string"
    || typeof req.body.dob != "string" || typeof req.body.address != "string") {
    return res.status(400).send({
      "error": true,
      "message": "Request body invalid: firstName, lastName, dob and address must be strings only"
    })
  }

  // 
  const email = req.params.email;
  let token = req.headers['authorization']

  if (!token) {
    return res.status(401).send({
      "error": true,
      "message": "Authorization header ('Bearer token') not found"
    })
  }
  if ((token.length <= 7) || (token.slice(0, 7) != 'Bearer ')) {
    return res.status(401).send({
      "error": true,
      "message": "Authorization header is malformed"
    })
  }
  token = token.slice(7, token.length);

  async function callback(err, bearerPayload) {
    if (err) {
      return res.status(401).send({
        "error": true,
        "message": "Invalid JWT token"
      })
    }
    if (bearerPayload['expire'] < Date.now()) {
      return res.status(401).send({
        "error": true,
        "message": "JWT token has expired"
      })
    }
    if (bearerPayload['email'] != email) {
      return res.status(403).send({
        "error": true,
        "message": "Forbidden"
      })
    }

    let person = await db.select('email').from('users').where('email', email);
    if (person.length != 1) {
      return res.status(404).send({
        "error": true,
        "message": "User not found"
      })
    }
    person = person[0]
    person['firstName'] = req.body.firstName;
    person['lastName'] = req.body.lastName;
    person['dob'] = req.body.dob;
    person['address'] = req.body.address;

    await db('users').where('email', email).update({
      'firstName': req.body.firstName,
      'lastName': req.body.lastName,
      'dob': req.body.dob,
      'address': req.body.address,
    })

    return res.send(person)
  }
  jwt.verify(token, 'secret', callback)
})

module.exports = router;
