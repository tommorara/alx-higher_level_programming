#!/usr/bin/node
const args = process.argv.length;
if (args === 3) {
  console.log('Argmument found');
} else if (args === 2) {
  console.log('No argmuent');
} else {
  console.log('Arguments found');
}
