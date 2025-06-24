#!/usr/bin/node
const num = Number(process.argv[2]);
if (!isNaN(num)) {
  console.log('C is fun\n'.repeat(num));
} else {
  console.log('Missing number of occurrences');
}
