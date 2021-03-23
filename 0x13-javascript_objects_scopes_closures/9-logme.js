#!/usr/bin/node
// Prints the current number of argument and the argument itself.

// Declare "global" scope argNum variable.
let argNum = 0;
// Declare exportable logMe function.
exports.logMe = function (item) {
  console.log(`${argNum}: ${item}`);
  argNum += 1;
};
