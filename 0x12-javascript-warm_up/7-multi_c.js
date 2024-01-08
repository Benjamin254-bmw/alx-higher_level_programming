#!/usr/bin/node
// Script that prints x times "C is fun"

if (isNaN(process.argv[2] || process.argv[2] === undefined)) {
    console.log("Missing number of occurences")
} else {
    let i = 0;
    while (Number(process.argv[2]) > i){
        console.log("C is fun");
        i++;
    }
}
