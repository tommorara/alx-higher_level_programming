#!/usr/bin/node
const x = Number(process.argv[2]);
if (!isNaN(x)) {
  for (let i = 1; i <= x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing nummber of occurrences');
}
