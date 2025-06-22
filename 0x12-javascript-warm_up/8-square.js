#!/usr/bin/node
const firstArg = process.argv[2];
const x = parseInt(firstArg);
if (!isNaN(x) || x < 0) {
  for (let i = 1; i <= x; i++) {
    console.log('x'.repeat(x));
  }
} else {
  console.log('Missing size');
}
