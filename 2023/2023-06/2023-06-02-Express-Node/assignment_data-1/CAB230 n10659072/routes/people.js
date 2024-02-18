var express = require('express');
var router = express.Router();
const db = require('../components/database')

router.get('/:id', async function (req, res, next) {
    //res.send('/movie/search');
    var id = req.params.id;

    const qrs = Object.keys(req.query)
    if (qrs.length != 0) {
        res.send({
            "error": true,
            "message": "Invalid query parameters: " + JSON.stringify(qrs) + ". Query parameters are not permitted."
        });
        return;
    }

    let row = await db.select('primaryName as name', 'birthYear', 'deathYear', 'knownForTitles').from('names').where('nconst', id)
    if (row.length != 1) {
        res.send({
            "error": true,
            "message": "No record exists of a person with this ID"
        })
        return;
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
    res.send(row);
});

module.exports = router;
