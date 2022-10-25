#!/usr/bin/node
// Class Square that has charPrint method
class Square extends require('./5-square') {
  charPrint (c) {
    super.print(c);
  }
}

module.exports = Square;
