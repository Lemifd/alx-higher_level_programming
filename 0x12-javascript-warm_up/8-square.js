#!/usr/bin/node
if (process.argv[2] && parseInt(process.argv[2])) {
  const len = process.argv[2];
  const sqr = 'X';
  for (let i = 0; i < len; i++) {
    console.log(sqr.repeat(len));
  }
} else {
  console.log('Missing size');
}
