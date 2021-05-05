#!/usr/bin/node
const request = require('request');
const GET = request.get;

const url = process.argv[2];

GET(url, (err, res, body) => {
  if (err) return (console.log(err));
  const data = JSON.parse(body);

  const tasks = {};

  for (let i = 0; i < data.length; i++) {
    if (data[i].completed) {
      const id = data[i].userId;
      tasks[id] !== undefined ? tasks[id] += 1 : tasks[id] = 1;
    }
  }
  console.log(tasks);
});
