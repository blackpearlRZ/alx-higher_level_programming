#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

for (let i = 2; i < 4; i++) {
  fs.readFile(argv[i], 'utf8', (err, data) => {
    if (err) {
      return;
    }

    fs.appendFileSync(argv[4], data, 'utf8');
  });
}
