#!/usr/bin/node
const arg = process.argv[2];
const number = parseInt(arg);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
