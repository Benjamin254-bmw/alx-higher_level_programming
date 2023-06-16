#!/usr/bin/node

const fs = reqire('fs');

const file1 = fs.readFileSync(process.argv[2]);
const file2 = fs.readFileSync(process.argv[3]);
const arr = [file1, file2];
let file = fs.createWriteStream(process.argv[4]);
arr.forEach(function (line) {
  file.write(line);
});
