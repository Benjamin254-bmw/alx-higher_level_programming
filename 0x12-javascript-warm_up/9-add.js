#!/usr/bin/node
function add(a, b){
return(parseInt(a) + parseInt(b));
}
console.log(add(Process.argv[2] + process.argv[3]));
