#!/usr/bin/node

const data = require('./100-data.js');
const list = data.list;

const newList = list.map((value, index) => value * index);

console.log('Initial list:', list);
console.log('New list:', newList);

