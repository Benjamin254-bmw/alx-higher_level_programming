#!/usr/bin/node
// Function incr that increments the integer value.

const myObject = {
    type: 'object',
    value: 12
  };
  console.log(myObject);
  
  myObject.value = function () {
    this.value++;
  }
  
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);