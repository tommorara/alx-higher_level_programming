#!/usr/bin/node
const num = Number(process.argv[2]);
if (!isNaN(num)) {
  console.log('My Number: ' + num);
} else {
  console.log('Not a number');
}
