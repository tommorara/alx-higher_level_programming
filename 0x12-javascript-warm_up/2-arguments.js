#!/usr/bin/node
const args = process.argv.length;
if (args === 2) {
  console.log('No arguments found');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
