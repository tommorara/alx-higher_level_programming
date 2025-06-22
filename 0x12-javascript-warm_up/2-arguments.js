#!/usr/bin/node
const number = process.argv.length;
if (number === 2) {
  console.log('No argument found');
} else if (number === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
