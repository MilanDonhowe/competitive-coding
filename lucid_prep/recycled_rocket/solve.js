const fs = require('fs')

const input = fs.readFileSync("in.bongo", encoding="ascii")
const items = input.split('\n').slice(1).map(ln => ln.split(' '))

let min = null

for (let [req, spare] of items) {
  const ratio = Math.floor(Number(spare) / Number(req))
  if ( min == null || ratio < min) {
    min = ratio
  }
}

console.log(min)