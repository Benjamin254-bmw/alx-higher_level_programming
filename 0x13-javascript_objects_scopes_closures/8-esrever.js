#!/usr/bin/node

exports.esrever = function (list) {
  const last = list.length - 1;
  let i;
  const arr = [];
  for (i = last; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
