#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Squire extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Squire;
