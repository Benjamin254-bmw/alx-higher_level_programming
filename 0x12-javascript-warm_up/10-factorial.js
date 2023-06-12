#!/usr/bin/node

function factorials (a){
if(isNaN(a)){
return 1;
}
if(a===1){
return 1;
} else {
return a * factorials(a-1);
}
}
console.log(factorials(parseInt(process.argv[2])));
