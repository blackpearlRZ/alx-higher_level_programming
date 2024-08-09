#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request.get(argv[2]).on('response', (response) => {
  console.log('code: ' + response.statusCode);
});
