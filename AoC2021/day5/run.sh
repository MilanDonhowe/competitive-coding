#!/bin/bash
echo "compiling solve.c"
gcc -Wall -std=gnu99 solve.c -o solve
echo "running solve program"
./solve test_input
./solve input
echo "cleaning up program"
rm -f solve
