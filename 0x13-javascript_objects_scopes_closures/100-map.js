#!/usr/bin/node

let list = require('./100-data').list;
const newList = [];

newList = list.map(function (n, i) {
  return n * i;
});

console.log(list);
console.log(newList);
