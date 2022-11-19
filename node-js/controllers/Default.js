'use strict';

var utils = require('../utils/writer.js');
var Default = require('../service/DefaultService');

module.exports.inverse_picture_picture_invert_get = function inverse_picture_picture_invert_get (req, res, next) {
  Default.inverse_picture_picture_invert_get()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.is_prime_number_prime__number__get = function is_prime_number_prime__number__get (req, res, next, number) {
  Default.is_prime_number_prime__number__get(number)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.root__get = function root__get (req, res, next) {
  Default.root__get()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.user_login_get = function user_login_get (req, res, next) {
  Default.user_login_get()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
