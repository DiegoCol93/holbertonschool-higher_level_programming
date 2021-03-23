#!/usr/bin/node
// Adds two int numbers passed as arguments.
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(process.argv[2], process.argv[3]);
