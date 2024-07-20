#!/usr/bin/node

const rib = Math.floor(Number(process.argv[2]));
if (isNaN(rib)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < rib; i++) {
    let coll = '';
    for (let c = 0; c < rib; c++) coll += 'X';
    console.log(coll);
  }
}
