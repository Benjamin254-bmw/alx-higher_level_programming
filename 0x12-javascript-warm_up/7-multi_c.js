#!/usr/bin/node
let num = parseInt(process.argv[2]);
while(i=0; i<num.length; i++){
console.log(num[i] * "C is fun");
}else if(num===undefined || isNaN(num)){
console.log("Missing number of occurrences");
}
