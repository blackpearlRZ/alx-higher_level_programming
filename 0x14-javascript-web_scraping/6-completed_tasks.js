#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const myDict = {};
  body.forEach((task) => {
    if (task.completed) {
      if (!myDict[task.userId]) {
        myDict[task.userId] = 1;
      } else {
        myDict[task.userId] += 1;
      }
    }
  });
  console.log(myDict);
});
