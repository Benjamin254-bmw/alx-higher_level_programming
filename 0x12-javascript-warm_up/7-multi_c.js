#!/usr/bin/node
let num = parseInt(process.argv[2]);

if (num === undefined || isNaN(num)){
console.log("Missing number of occurrences");
}else {
for (i=0; i<num; i++){
console.log("C is fun");
}
}
