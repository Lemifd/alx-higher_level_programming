#!/usr/bin/node
// Function that returns the number of occurences in a list
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const item of list) {
    if (item === searchElement) {
      occurences += 1;
    }
  }
  return occurences;
};
