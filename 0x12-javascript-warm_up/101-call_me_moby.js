#!/usr/bin/node
// Executes x times a function.
module.exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
};
