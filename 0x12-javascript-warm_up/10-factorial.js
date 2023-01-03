#!/usr/bin/node
function factorial (x) {
  if (!x || x === 0) {
    return 1;
  }
  return factorial(x - 1) * x;
}
console.log(factorial(process.argv[2]));
