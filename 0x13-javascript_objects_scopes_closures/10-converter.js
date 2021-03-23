#!/usr/bin/node
// Converts a number from base 10 to another base.
exports.converter = function (base) {
  return (x) => x.toString([base]);
};

// One liner for the same function above.
// exports.converter = base => (x) => x.toString([base]);
