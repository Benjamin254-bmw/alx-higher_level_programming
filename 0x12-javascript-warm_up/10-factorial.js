#!usr/bin/node
let a = parseInt(a);

function factorials (a){
if(isNaN(a)){
return 1;
}else{
if(a===1){
return 1;
} else {
return a * factorials(n-1);
}
}
}
console.log(factorials(parseInt(process.argv[2])));
