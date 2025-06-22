#!/usr/bin/node
const argCount = process.argv.length;
if (argCount === 2) {
  console.log("No argument found");
} else if (argCount === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
