var express = require('express');
var router = express.Router();
const db = require('../components/database')

router.get('/search', async function (req, res, next) {
  //res.send('/movie/search');
  var title = req.query.title;
  var year = parseInt(req.query.year);
  var page = parseInt(req.query.page);
  page = isNaN(page) ? 1 : page;

  if (year && (year < 1000 || year > 9999 || isNaN(year))) {
    res.send({
      "error": true,
      "message": "Invalid year format. Format must be yyyy."
    })
    return;
  }

  let tmp = db.select('primaryTitle as title', 'year', 'tconst as imdbID', 'imdbRating',
    'rottenTomatoesRating as rottentomatoesRating', 'metacriticRating', 'rated as classification').from('basics');
  if (title) {
    tmp = tmp.where('primaryTitle', title).orWhere('originalTitle', title);
  }
  if (year) {
    tmp = tmp.where('year', year);
  }
  const rows = await tmp.orderBy('imdbID', 'asc');
  const pagination = {
    "total": rows.length,
    "lastPage": Math.max(Math.ceil(rows.length / 100), 1),
    "perPage": 100,
    "currentPage": page,
    "from": 100 * (page - 1),
    "to": Math.min(100 * page - 1, rows.length)
  }

  res.send({ "data": rows.slice(pagination["from"], pagination["to"]), "pagination": pagination });
});

router.get('/data/:imdbID', async function (req, res, next) {
  //res.send('/movie/data/:imdbID');
  try {
    let id = req.params.imdbID;
    id = id ? id : "";

    const qrs = Object.keys(req.query)
    if (qrs.length != 0) {
      res.send({
        "error": true,
        "message": "Invalid query parameters: " + JSON.stringify(qrs) + ". Query parameters are not permitted."
      });
      return;
    }

    let row = await db.select('primaryTitle as title', 'year', 'runtimeMinutes as runtime', 'genres',
      'country', 'boxoffice', 'poster', 'plot').from('basics').where('tconst', id)
    if (row.length != 1) {
      res.send({
        "error": true,
        "message": "No record exists of a movie with this ID"
      })
      return;
    }
    row = row[0]
    row['genres'] = row['genres'].split(",")
    row['country'] = row['country'].split(",")
    if (row['genres'].length == 1) {
      row['genres'] = row['genres'][0];
    }
    if (row['country'].length == 1) {
      row['country'] = row['country'][0];
    }

    // ratings
    var ratings = await db.select('source', 'value').from('ratings').where('tconst', id);
    for (let i = 0; i < ratings.length; i++) {
      ratings[i]['value'] = parseFloat(ratings[i]['value'])
      // const split1 = ratings[i]['value'].split("%");
      // const split2 = ratings[i]['value'].split("/");
      // if (split1.length == 2) {
      //   ratings[i]['value'] = parseFloat(split1[0]);
      // }
      // else {
      //   ratings[i]['value'] = parseFloat(split2[0]) / parseFloat(split2[1]);
      // }
    }
    row["ratings"] = ratings;

    // principals
    let principals = await db.select('id', 'category', 'name', 'characters').from('principals').where('tconst', id);
    for (let i = 0; i < principals.length; i++) {
      principals[i]['characters'] = principals[i]['characters'] == '' ? [] : JSON.parse(principals[i]['characters']);
    }
    row['principals'] = principals;

    res.send(row);
  }
  catch (err) {
    res.status(404).send('404 Not Found');
  }
});



module.exports = router;
