/*
  Power Set: Write method to return all subsets of a set.
*/

#include <bits/stdc++.h>
#include <cstdint>
using namespace std;

typedef int64_t ll;
typedef int32_t num;
typedef __int128_t big;

void power_set_step(vector<vector<ll>> &power_set, vector<ll> &original_set, ll place){
  ll size = power_set.size();
  for (int i = 0; i < size; i++){
    vector<ll> new_subset = power_set[i];
    new_subset.push_back(original_set[place]);
    power_set.push_back(new_subset);
  }
  vector<ll> addition (1, original_set[place]);
  power_set.push_back(addition);
}

int main(int argc, char** argv){
  ios::sync_with_stdio(0);
  cin.tie(0);

  vector<ll> input_set;
  ll size;
  cin >> size;
  for (int i=0; i < size; i++){
    ll num;
    cin >> num;
    input_set.push_back(num);
  }

  vector<vector<ll>> power_set;
  for (int i=0; i < size; i++){
    power_set_step(power_set, input_set, i);
  }

  for (size_t i=0; i< power_set.size(); i++){
    cout << "{" << power_set[i][0];
    for (size_t j=1; j<power_set[i].size();j++){
      cout << ", " << power_set[i][j];
    }
    cout << "}\n";
  }

	// freopen("file.txt", "r", stdin);
  // freopen("ouput.txt", "w", stdout);

	return 0;
}
