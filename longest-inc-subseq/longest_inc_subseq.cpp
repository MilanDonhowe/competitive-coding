/*
 * This problem is the longest increasing sub-sequence
 * */

#include <bits/stdc++.h>
using namespace std;



int longest_subseq(vector<int> &seq){
	
	// initialize them all by asssuming they are at best 1
	vector<int> l (seq.size(), 1);

	for (int pos=1; pos < seq.size(); pos++){
		// for array [pos] we need to find
		// the longest subsequence s.t. we
		// can fit the current item atop it
		int best = pos;
		for (int i=0; i < pos; i++){
			// is it valid?
			if (seq[i] < seq[pos] && l[i] >= l[best]){
				best = i;
			}
		}

		if (pos != best) l[pos] = l[best] + 1;

	}
	
	int maxl = 0;
	for (auto num : l){
		maxl = max(maxl, num);
	}

	return maxl;
}


int main(){
	vector<int> seq = {6, 2, 5, 1, 7, 4, 8, 3};
	cout << longest_subseq(seq) << '\n';
	return 0;
}
