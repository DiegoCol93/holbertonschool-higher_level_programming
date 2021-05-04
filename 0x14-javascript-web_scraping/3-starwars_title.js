#!/usr/bin/node
const request = require('request');
const GET = request.get;
const url = 'https://swapi-api.hbtn.io/api/films/';
const number = Number(process.argv[2]);

GET(url, (err, response, body) => {
  if (err) return (console.log(err));

  const data = JSON.parse(body);
  const movies = data.results;

  for (let i = 0; i < movies.length; i++) {
    if (movies[i].episode_id === number) {
      console.log(movies[i].title);
    }
  }
});
