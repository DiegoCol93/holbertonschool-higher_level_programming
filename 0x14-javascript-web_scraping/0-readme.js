#!/usr/bin/node

const fs = require('fs');
const rf = fs.readFile;

const av = process.argv;

rf(av[2], 'utf8', (err, data) => {
  if (err) return (console.log(err));
  console.log(data);
});
