#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const entry in dict) {
  if (!newDict[dict[entry]]) {
    newDict[dict[entry]] = [];
  }
  newDict[dict[entry]].push(entry);
}

console.log(newDict);
