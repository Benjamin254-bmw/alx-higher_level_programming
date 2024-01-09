#!/use/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.hight = h;
      print() {
        console.log('X');
      }
    }
  }
}
