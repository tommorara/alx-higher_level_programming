#!/usr/bin/node
const firstArg = process.argv[2];
const x = parseInt(firstArg);
let i = 1;
if (!isNaN(x)) {
  while (i <= x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurences');
}
