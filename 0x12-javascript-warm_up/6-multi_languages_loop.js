#!/usr/bin/node
// Script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

const C = 'C is fun';
const Python = 'Python is cool';
const JavaScript = 'JavaScript is amazing';
const langs = [C, Python, JavaScript];

for (const line of langs) {
  console.log(line);
}
