// generate template
const fs = require('fs')
const path = require('path')

const args = process.argv

if (args.length != 3){
	console.log('bad hooman!  make sure to specify the problem name!')
	console.log(`correct usage: ${args[0]} ${args[1]} <problem name>`)
	process.exit(0)
}

const problem = process.argv[2]

const makefile = `
CC=g++
CFLAGS=-O2 -Wall -std=c++11
PROG=${problem}

$(PROG): $(PROG).cpp
	$(CC) $< $(CFLAGS) -o $(PROG)
clean:
	rm -f $(PROG)
`

const cpp = `
#include <bits/stdc++.h>
#include <cstdint>
using namespace std;

typedef int64_t ll;
typedef int32_t num;
typedef __int128_t big;

int main(int argc, char** argv){
  ios::sync_with_stdio(0);
  cin.tie(0);
	
	// freopen("file.txt", "r", stdin);
  // freopen("ouput.txt", "w", stdout);

	return 0;
}
`

if (fs.readdirSync(__dirname).includes(problem)){
	console.log(`bad hooman!  a directory with that name already exists! >:C`)
}

fs.mkdirSync(problem)
fs.writeFileSync(path.join(__dirname, problem, 'makefile'),  makefile)
fs.writeFileSync(path.join(__dirname, problem, `${problem}.cpp`), cpp)
console.log("DONE hooman.")


