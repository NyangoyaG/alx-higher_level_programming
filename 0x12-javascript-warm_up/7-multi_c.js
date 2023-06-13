#!/usr/bin/node
const process = require('process');
let times = parseInt(process.argv[2]);
const message1 = 'Missing number of occurrences';
const message2 = 'C is fun';
if (isNaN(times)) {
  console.log(message1);
} else {
  while (times > 0) {
    console.log(message2);
    times--;
  }
}
