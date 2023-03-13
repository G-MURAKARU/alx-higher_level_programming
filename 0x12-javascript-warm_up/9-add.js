#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const a = parseFloat(process.argv[2]);
const b = parseFloat(process.argv[3]);
if (isNaN(a) || isNaN(b)) {
  // nothing
} else {
  add(a, b);
}
