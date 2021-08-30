/*
  The classic 0-1 Knapsack problem.

  Given a set of objects each which a weight & value find the highest value
  combination of items that fit into a knap-sack with a discrete maximum carrying
  capacity.
*/
#include <bits/stdc++.h>
#include <cstdint>
using namespace std;

typedef int64_t ll;
typedef int32_t num;
typedef __int128_t big;

ll max (ll a, ll b){
  return (a > b) ? a : b;
}

ll knapsack(ll *weights, ll* values, int size, ll capacity){
  // Create table of capacity rows which item number of items
  vector< vector<ll> > table (capacity+1, vector<ll> (size, 0));

  for (int cap = 1; cap < capacity+1; cap++){
    for (int item = 0; item < size; item++){
      // Can we fit this item in our bag?
      if (weights[item] > cap){
        // we can't fit the item in the bag
        if (item != 0) table[cap][item] = table[cap][item-1];
      } else {
        // we can fit the item in the bag
        // is our bag higher value with the item--or without it?
        if (item != 0) {
          table[cap][item] = max ( table[cap-weights[item]][item-1] + values[item], table[cap][item-1] );
        } else {
          table[cap][item] = values[item];
        }
      }
    }
  }

  return table[capacity][size-1];
}

int main(int argc, char** argv){
  ios::sync_with_stdio(0);
  cin.tie(0);

  /*
  const int num_items = 9;
  ll weights[] = {10, 20, 40, 50, 12, 30, 94, 12, 43};
  ll values[] =  {9,  21, 4,  8,  15, 40, 23, 45, 12};
  const ll capacity = 65; 
  */

  /*  
  const int num_items = 3;
  ll weights[] = {10, 20, 30};
  ll values[] =  {60, 100, 120};
  const ll capacity = 50;
  */

  const int num_items = 10;
  ll weights[] = {23, 26, 20, 18, 32, 27, 29, 26, 30, 27};
  ll values[] =  {505, 352, 458, 220, 354, 414, 498, 545, 473, 543};
  const ll capacity = 67;


  cout << knapsack(weights, values, num_items, capacity) << '\n';
	
	// freopen("file.txt", "r", stdin);
  // freopen("ouput.txt", "w", stdout);

	return 0;
}
