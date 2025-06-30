#!/usr/bin/node

// Import the list from the file
const { list } = require('./100-data.js');

// Compute a new array using map
const newList = list.map((current, index) => current * index);

// Print the initial list
console.log(list);

// Print the new list
console.log(newList);
