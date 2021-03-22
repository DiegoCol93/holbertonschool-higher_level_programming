#!/usr/bin/node
// Prints a square of x size.
//
//   Useage: ./8-square.js {# Size of square}

// If Not A Number.
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  // For i = given number and greater than 0.
  for (let i = Number(process.argv[2]); i > 0; i--) {
    console.log('x'.repeat(process.argv[2]));
  }
}
