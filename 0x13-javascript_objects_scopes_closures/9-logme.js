#!/usr/bin/node
// Function that prints the number of arguments already printed and the argument passed.
let args = 0;
exports.logMe = function (item) {
  console.log(`${args}: ${item}`);
  args += 1;
};
