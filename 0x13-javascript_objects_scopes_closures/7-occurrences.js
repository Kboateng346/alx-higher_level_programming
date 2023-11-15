#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, item) =>
    (item === searchElement ? ++count : count), 0
  );
};
