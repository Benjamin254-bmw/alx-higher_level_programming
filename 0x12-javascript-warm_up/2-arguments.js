#!/usr/bin/node

// Script that prints a message depending of the number of arguments passed:
if (process.argv.length === 2){
    console.log('No argument');
} else if (process.argv.lenght === 3){
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
