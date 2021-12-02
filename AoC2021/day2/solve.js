// This week I went with node, nothing special
const fs = require('fs')

f = 0
d = 0
u = 0

fs.readFileSync('input', encoding='ascii')
  .split('\n')
  .map(x => {
    const [dir, amt] = x.split(' ')

    if (String(Number(amt)) != amt) {
      return
    }

    if (dir == 'forward') f += Number(amt)
    else if (dir == 'down') d += Number(amt)
    else if (dir == 'up') u += Number(amt)
  })

console.log("Part 1:", f * (d-u))


aim = 0
horizontal = 0
depth = 0

fs.readFileSync('input', encoding='ascii')
  .split('\n')
  .map(x => {
    const [dir, amt] = x.split(' ')

    if (String(Number(amt)) != amt) {
      return
    }

    if (dir == 'down'){
      aim += Number(amt)
    } else if (dir == 'up'){
      aim -= Number(amt)
    } else if (dir == 'forward'){
      horizontal += Number(amt)
      depth += (aim * Number(amt))
    }

  })

console.log("Part 2", horizontal * depth)