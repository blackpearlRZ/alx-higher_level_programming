#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const charId = '18';
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const bodyJson = JSON.parse(body);
    bodyJson.results.forEach((film) => {
      film.characters.forEach((Actor) => {
        if (Actor.includes(charId)) {
          count++;
        }
      });
    });
  }
  console.log(count);
});
