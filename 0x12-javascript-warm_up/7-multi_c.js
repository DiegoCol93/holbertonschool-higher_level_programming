#!/usr/bin/node
// Prints 'C is fun' a number of given times.
//
//   Useage: ./7-multi_c.js {# of times}
//

// If Not A Number.
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  // For number given is more than 0.
  for (let i = Number(process.argv[2]); i > 0; i--) {
    console.log('C is fun');
  }
}
