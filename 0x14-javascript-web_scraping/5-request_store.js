#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    console.log(body);
  } else {
    fs.writeFile(fileName, body, 'UTF-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
