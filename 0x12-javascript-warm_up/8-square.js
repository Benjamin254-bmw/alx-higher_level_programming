#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (i=0; i<num; i++) {
    console.log('X');
    let s='';
    for(x=0; x<num; x++) {
    s+='X';
    }
    console.log(s);
  }
}
