#!/usr/bin/node
const A = require('./5-square.js');
module.exports = class Square extends A {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = this.height; i > 0; i--) {
        console.log(`${c}`.repeat(this.width));
      }
    }
  }
};
