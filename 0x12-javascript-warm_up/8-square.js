i#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
    }
  }
