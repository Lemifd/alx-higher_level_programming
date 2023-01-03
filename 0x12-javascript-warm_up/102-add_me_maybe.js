#!/usr/bin/node
const addMeFunc = function (number, theFunction) {
  theFunction(++number);
};

exports.addMeMaybe = addMeFunc;
