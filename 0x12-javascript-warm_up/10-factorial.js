#!/usr/bin/node

function factorialof (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorialof(n - 1);
}
console.log(factorialof(Number(process.argv[2])));
