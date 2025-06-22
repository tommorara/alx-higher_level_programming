#!/usr/bin/node
const countArg = process.argv.length;

if (countArg === 2) {
  console.log('No argument');
} else if (countArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
