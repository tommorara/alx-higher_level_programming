#!/usr/bin/env node

// Checking the number of arguments passed (excluding the node path and file path)
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('No argument');
} else if (args.length === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}

