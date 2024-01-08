#!/usr/bin/node
// Script that prints the first argument passed to it:

if (Process.argv[2] === undefined){
    console.log("No argument");
} else {
console.log(process.argv[2]);
}