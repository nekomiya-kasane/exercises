var express = require('express');
var passport = require('passport');
var router = express.Router();

router.use(passport.authenticate('jwt', { session: false }));

/* GET user listing. */

router.get('/:email/profile', function(req, res, next) {
  let email = req.params.email;

});

router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

module.exports = router;
