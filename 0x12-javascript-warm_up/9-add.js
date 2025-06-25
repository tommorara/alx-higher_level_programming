#!/usr/bin/node
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
function add (a, b) {
  if (!isNaN(a) & !isNaN(b)) {
    console.log(a + b);
  } else {
    console.log(a + b);
  }
}

add(a, b);
