/*
 *------{n x n pathways problem}------------------------------------
 * when given an n by n grid compute the total number of pathways
 * which go from the top-left corner to the bottom-right while still
 * crossing every single square.
 *
 * In order to solve this problem in a semi-reasonable time we must
 * add optimizations where we "prune" specific pathways we know
 * won't result in a solution.
 **/
#include <bits/stdc++.h>
using namespace std;

unsigned long long calls = 0;

bool in_bounds(const pair<int,int> loc, const int &max){
	if (loc.first < 0 || loc.first >= max) return false;
	if (loc.second < 0 || loc.second >= max) return false;
	return true;
}

enum direction {
	LEFT = 0,
	RIGHT = 1,
	UP = 3,
	DOWN = 4

};

void paths(set<pair<int,int>> visited, pair<int, int> pos, direction prev, const int &MAX, int &total){
	// an even board has 0 pathways
	if ( (MAX & 1) == 0) return;
	visited.insert(pos);
	calls++;
	//cout << pos.first << ", " << pos.second << " visited.size == " << visited.size() << "\n";
	if (pos.first == MAX-1 && pos.second == MAX-1) {
		if (visited.size() == MAX * MAX){
			total++;
		}
		return;
	}
	// premature exit conditions
	if (visited.size() == MAX*MAX) return;

	pair<int, int> up   (pos.first, pos.second-1);
	pair<int, int> down (pos.first, pos.second+1);
	pair<int, int> left (pos.first-1, pos.second);
	pair<int, int> right (pos.first+1, pos.second);


	bool CAN_MOVE_UP = in_bounds(up, MAX) && visited.count(up) == 0;
	bool CAN_MOVE_DOWN = in_bounds(down, MAX) && visited.count(down) == 0;
	bool CAN_MOVE_LEFT = in_bounds(left, MAX) && visited.count(left) == 0;
	bool CAN_MOVE_RIGHT = in_bounds(right, MAX) && visited.count(right) == 0;

	// CHECK BRANCH CONDITIONS (where there will be unreachable squares)
	if (pos.first == MAX-1 || pos.first == 0){
		if (CAN_MOVE_UP && CAN_MOVE_DOWN) return; 
	}

	if (pos.second == MAX-1 || pos.second == 0){
		if (CAN_MOVE_LEFT && CAN_MOVE_RIGHT) return;
	}
	// if you cannot move forward but can branch then you won't pass every square
	if (prev == LEFT && !CAN_MOVE_LEFT && CAN_MOVE_UP && CAN_MOVE_DOWN) return;
	if (prev == RIGHT && !CAN_MOVE_RIGHT && CAN_MOVE_UP && CAN_MOVE_DOWN) return;
	if (prev == UP && !CAN_MOVE_UP && CAN_MOVE_LEFT && CAN_MOVE_RIGHT) return;
	if (prev == DOWN && !CAN_MOVE_DOWN && CAN_MOVE_LEFT && CAN_MOVE_RIGHT) return;

	if (CAN_MOVE_UP)    paths(visited, up,  UP, MAX, total);
	if (CAN_MOVE_DOWN)  paths(visited, down, DOWN, MAX, total);
	if (CAN_MOVE_LEFT)  paths(visited, left, LEFT, MAX, total);
	if (CAN_MOVE_RIGHT) paths(visited, right,RIGHT, MAX, total);
}

int main(int argc, char **argv){
	ios::sync_with_stdio(0);
	cin.tie();
	
	const int max = atoi(argv[1]);	
	int total = 0;
	// we start by moving right since every path
	// has another symmetric version where you start
	// by going down first instead.
	set<pair<int, int>> cache;
	cache.insert(pair<int, int>(0, 0));
	paths(cache, pair<int,int>(0, 1), RIGHT, max, total);

	cout << calls << " total function calls\n" << total*2 << " paths found\n";
	return 0;
}
