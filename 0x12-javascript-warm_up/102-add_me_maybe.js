#!/usr/bin/node
// A function that increments and calls a function

exports.multMeMaybe = function (number, theFunction) {
    theFunction(++number);
};