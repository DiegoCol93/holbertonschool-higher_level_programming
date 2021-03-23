#!/usr/bin/node
// Computes and prints the factorial of a given number.

// Define recursive factorial function.
function factorial (n) {
  let result = 1;
  if (n > 0) {
    result = n * factorial(n - 1); // Begin recursion, result = n * (n - 1) * (n - 2)...
  }
  return result;
}
// Check if Not A Number.
if (isNaN(parseInt(process.argv[2]))) {
  console.log(1);
} else {
  // Call factorial function.
  console.log(factorial(parseInt(process.argv[2])));
}
