#!/usr/bin/node
// Computes and prints the factorial of a given number.

// Check if Not A Number.
if (isNaN(parseInt(process.argv[2]))) {
  console.log(1);
} else {
  // Define recursive factorial function.
  function factorial (n) {
    let result = 1;
    // Base Case.
    if (n > 0) {
      // Begin recursion.
      // result = n * (n - 1) * (n - 2)...
      result = n * factorial(n - 1);
    }
    return result;
  }
  // Call factorial function.
  console.log(factorial(parseInt(process.argv[2])));
}
