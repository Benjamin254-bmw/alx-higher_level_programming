#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (num === undefined || isNaN(num)){
console.log(Missing size);
} else {
for (i=0; i<num; i++){
console.log("X");
for(x=0; x<i; x++){
console.log("X");
}
}
}
