#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments

if (process.argv.length < 2 || process.argv[2) === undefined {
  console.log(0);
} else {
  const arr = process.argv.slice(2).map(Number);
  const second = arr.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
