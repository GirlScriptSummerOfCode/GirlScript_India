var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('app', { title: 'GirlScript_India'});
});

module.exports = router;
