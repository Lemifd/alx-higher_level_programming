#!/usr/bin/node
// Function that reverses a list
exports.esrever = function (list) {
  const rev = [];
  for (let ind = list.length - 1; ind >= 0; ind--) {
    rev.push(list[ind]);
  }
  return rev;
};
