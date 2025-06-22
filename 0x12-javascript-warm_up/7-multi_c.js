#!/usr/bin/node
const firstArg = process.argv[2];
const x = parseInt(firstArg);
if (!isNaN(x)) {
  for (let i = 1; i <= x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurances');
}
