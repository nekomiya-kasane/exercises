var express = require('express');
var router = express.Router();
const db = require('../components/database')
const jwt = require('jsonwebtoken');

var bl = require('./var')
blacklist = bl.blacklist

router.get('/:id', async function (req, res, next) {
    let token = req.headers.authorization;
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

        return undefined;
    }

    let verifyResult = await jwt.verify(token, 'secret', callback)
    if (verifyResult) {
        return verifyResult;
    }

    var id = req.params.id;

    const qrs = Object.keys(req.query)
    if (qrs.length != 0) {
        return res.status(400).send({
            "error": true,
            "message": "Invalid query parameters: " + JSON.stringify(qrs) + ". Query parameters are not permitted."
        });;
    }

    let row = await db.select('primaryName as name', 'birthYear', 'deathYear', 'knownForTitles').from('names').where('nconst', id)
    if (row.length != 1) {
        return res.status(404).send({
            "error": true,
            "message": "No record exists of a person with this ID"
        });
    }
    row = row[0]

    const tts = row['knownForTitles'].split(',')
    let roles = []
    for (let i = 0; i < tts.length; i++) {
        let item1 = await db.select('primaryTitle as movieName', 'tconst as movieId', 'imdbRating').from('basics').where('tconst', tts[i])
        let item2 = await db.select('category', 'characters').from('principals').where('tconst', tts[i]).andWhere('nconst', id)
        if (!item1 || !item2 || !item1.length || !item2.length) {
            continue;
        }
        item1 = item1[0]
        item2 = item2[0]
        item1['imdbRating'] = item1['imdbRating'] ? parseFloat(item1['imdbRating']) : null
        item2['characters'] = item2['characters'] == '' ? [] : JSON.parse(item2['characters']);
        roles.push(Object.assign({}, item1, item2))
    }
    delete row.knownForTitles;
    row["roles"] = roles;
    return res.send(row);
});

module.exports = router;
