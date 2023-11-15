#!/usr/bin/node

const fs = require('fs');

const file0 = fs.readFileSync(process.argv[2], 'utf8');
const file1 = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], file0 + file1);
