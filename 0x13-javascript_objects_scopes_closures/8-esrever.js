#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];

  while (list.length) {
    reversed.push(list.pop());
  }

  return reversed;
};
