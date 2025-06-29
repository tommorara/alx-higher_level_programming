#!/usr/bin/node
const arg1 = process.argv[2];
if (arg1 === undefined) {
  console.log('No argument');
} else {
  console.log(arg1);
}
