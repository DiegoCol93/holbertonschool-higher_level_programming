#!/usr/bin/node
// Prints the second biggest integer in the list of arguments.

// Check if correct number of arguments.
if (process.argv.length < 4) {
  console.log(0);
} else {
  // Slice out the name and interpreter args.
  // Map Parsefloat function to all values to get signed ints.
  // Sort from highest to lowest.
  const numArray = process.argv.slice(2).map(parseFloat).sort(function (a, b) { return b - a; });
  // Print second value on array.
  console.log(numArray[1]);
}
