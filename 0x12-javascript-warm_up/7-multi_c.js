#!/usr/bin/node
const x = Number(process.argv[2]);
let i = 1;
if (!isNaN(x)) {
  while(i <= x) {
    console.log('C is fun'); 
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
  
