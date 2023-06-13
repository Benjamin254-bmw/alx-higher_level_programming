#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    let rows, columns;
    if (rows = 0; rows < this.width; rows++) {
      if (columns = 0; columns < this.height; columns++) {
        str += 'X';
      }
      console.log(str);
    }
  }
  rotate() {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double() {
    this.width *=2;
    this.height *=2;
  }
}

module.exports = Rectangle;
