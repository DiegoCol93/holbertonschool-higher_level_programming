#!/usr/bin/node
const request = require('request');
const GET = request.get;

const number = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + number;

// Declare Promise wrapper for GET method.
const getPromise = charUrl => new Promise((resolve, reject) => {
  GET(charUrl, (err, res, body) => {
    if (err) return (reject(err));
    resolve(JSON.parse(body).name);
  }, 300);
});

// Empty list for promises.
const promiseArray = [];

// Start GET request.
GET(url, (err, res, body) => {
  if (err) return (console.log(err));
  const movies = JSON.parse(body);

  // Start requesting the promises.
  movies.characters.forEach(charUrl => {
    promiseArray.push(getPromise(charUrl));
  });

  // Start executing the promises.
  Promise.all(promiseArray).then((values) => {
    values.forEach(name => (console.log(name)));
  }).catch(error => console.log(error));
});
