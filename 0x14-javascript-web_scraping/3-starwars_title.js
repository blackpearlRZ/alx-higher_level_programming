#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const bodyJson = JSON.parse(body);
    console.log(bodyJson.title);
  }
});
