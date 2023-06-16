#!/usr/bin/node
const dict = require('./101-data').dict;
const d = {};

for (const l in dict) {
  if (!(dict[l] in d)) {
    d[dict[l]] = [l];
  } else {
    d[dict[l]].push(l);
  }
}

console.log(d);
