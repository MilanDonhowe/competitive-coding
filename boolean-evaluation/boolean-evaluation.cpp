/*
  Boolean Evaluations
  Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
  (AND), | (OR), and ^ (XOR) and a desired boolean result, implement a function
  to count the number of ways of parenthesizing the expression s.t. it evaluates
  to result.  The expression should be fully parenthesized (0)^(1) but not
  extraneously like (((0))^((1))).

  EXAMPLE:
    countEval("1^0|0|1", false) --> 2
    countEval("0&0&0&0&1^1|0", true) --> 10
*/
#include <bits/stdc++.h>
#include <cstdint>
using namespace std;

typedef int64_t ll;
typedef int32_t num;
typedef __int128_t big;
/*
  Brainstorm:
    Well, we can start by parenthesizing each operand.

*/

char eval(char a, char op, char b){
  char result = 'e';
  switch (op) {
    case '^':
      result = (a-48) ^ (b-48);
      break;
    case '|':
      result = (a-48) | (b-48);
      break;
    case '&':
      result = (a-48) & (b-48);
      break;
    default:
      cout << "Error, non-triggered operator " << op << endl;
      exit(2);
  }
  return result;
}

/*

  Algorithm:
    1. Generate all parenthesized expressions.
    2. Evaluate all of them & count which ones yield the desired result.

*/

char r_eval(string exp, bool result){
  if (exp.size() > 3){
    return eval(exp[0], exp[1], r_eval(exp.substr(2), result));
  }
  return eval(exp[0], exp[1], exp[2]);
}


ll countEval(string expression, bool result){
  ll counter = 0;

  return counter;
}

int main(int argc, char** argv){
  ios::sync_with_stdio(0);
  cin.tie(0);
	
  string expression;
  cin >> expression;
	// freopen("file.txt", "r", stdin);
  // freopen("ouput.txt", "w", stdout);

	return 0;
}
