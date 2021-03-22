#!/usr/bin/node
// Prints a square of x size.
//
//   Useage: ./8-square.js {# Size of square}

// If Not A Number.
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  // For i and j = number given and are more than 0.
  for (let i = Number(process.argv[2]); i > 0; i--) {
    for (let j = Number(process.argv[2]); j > 0; j--) {
      process.stdout.write('x');
    }
    console.log();
  }
}
