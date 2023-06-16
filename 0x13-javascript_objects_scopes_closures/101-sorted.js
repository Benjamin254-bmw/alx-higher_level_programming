#!/usr/bin/node
let dict = require('./101-data').dict;
let d = {};

for (let l in dict) {
  if (!(dict[l]) in d) {
    d[dickt[l]] = [l];
  } else {
    d[dict[l]].push(l);
  }
}

console.log(d);
