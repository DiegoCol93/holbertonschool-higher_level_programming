#!/usr/bin/node
// Prints the first argument given "No argument" if no argument was given.
if (process.argv[2]) {
  console.log(`${process.argv[2]}`);
} else {
  console.log('No argument');
}
