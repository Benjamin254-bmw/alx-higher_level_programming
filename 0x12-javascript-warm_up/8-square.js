#!/usr/bin/node
// Script that prints a square

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const l = process.argv[2];
  let i = 0;
    
  while (l > i) {
    console.log('X'.repeat(l));
    i++;
  }
}
