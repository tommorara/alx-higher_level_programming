#!/usr/bin/node
const firstArg = process.argv[2];
const x = parseInt(firstArg);
let i = 1;
if (!isNaN(x) || x <= 0) {
  while (i <= x) {
    console.log('x'.repeat(x));
    i++;
  }
} else {
  console.log('Missing size');
}
