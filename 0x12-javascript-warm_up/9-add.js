#!/usr/bin/node
// Script that prints the addition of 2 integers

const a = process.argv[2];
const b = process.argv[3];

function add( a, b) {
  console.log(a + b);
}
add(Number(a), Number(b));
