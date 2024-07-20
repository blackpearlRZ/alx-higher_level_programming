#!/usr/bin/node

const argu = process.argv[2];

if (argu === undefined) {
  console.log('No argument');
} else {
  console.log(argu);
}
