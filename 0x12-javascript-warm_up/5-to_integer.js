#!/usr/bin/node
const fisrtArg = process.argv[2];
const number = parseInt(fisrtArg);
if (!isNaN(number)) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
