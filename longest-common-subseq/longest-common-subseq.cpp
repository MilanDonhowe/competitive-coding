/*
  Longest common subsequence problem

  This problem we have to find the longest common subsequence between strings

  Take two words: Halloween and When
  
  Two longest subsequence is H-E-N or W-E-N

*/
#include <bits/stdc++.h>
#include <cstdint>
using namespace std;

typedef int64_t ll;
typedef int32_t num;
typedef __int128_t big;


/*

  Let LCS be the function we wwnt (lol) 

  1. lcs (...a, ...a) = lcs(...) + a
  2. lcs (...a, ...b) = max{ lcs(...) + a, lcs(...) + b}
  3. lcs (0) = 0

  With these properties we make the algorithm (◡‿◡)
*/

string lcs (string A, string B) {
  // Create our table (gross stl syntax)
  vector<vector<int>> table ( A.size()+1, vector<int>(B.size()+1, 0) );
  for (size_t i = 1; i < A.size()+1; i++) {
    for (size_t j = 1; j < B.size()+1; j++) {
      if (A[i-1] == B[j-1]) {
        table[i][j] = table[i][j-1] + 1;
      } else {
        bool flag = table[i-1][j] > table[i][j-1];
        table[i][j] = (flag) ? table[i-1][j] : table[i][j-1];
      }
    }
  }
  
  //return table[A.size()][B.size()];
  
  // Traverse table for subsequence
  // this doesn't seem to work...
  string subsequence;
  size_t b = B.size();
  size_t a = A.size();
  while ( (a > 0) && (b > 0)) {
    if ( table[a-1][b] == table[a][b-1] ) {
      a--;
      b--;
    } else if (table[a-1][b] < table[a][b-1]) {
      subsequence += A[a-1];
      a--;
    } else {
      subsequence += B[b-1];
      b--;
    }
  }

  return subsequence;
}


int main(int argc, char** argv){
  ios::sync_with_stdio(0);
  cin.tie(0);
	
  cout << lcs("HALLOWEEN","WHEN") << endl;
	// freopen("file.txt", "r", stdin);
  // freopen("ouput.txt", "w", stdout);

	return 0;
}
