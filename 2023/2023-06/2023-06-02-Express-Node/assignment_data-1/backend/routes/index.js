var express = require('express');
var router = express.Router();

//const swaggerUI = require('swagger-ui-express')
//const swaggerDoc = require('swagger-jsdoc')

/* GET home page. */
// app.use('/swagger', swaggerUI.serve, swaggerUI.setup(swaggerSpec));

router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
