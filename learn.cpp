#include <bits/stdc++.h>

using namespace std;

/*----------------------------------------------------
 * [Milan's Tips & Tricks to Competitive Programming]
 *----------------------------------------------------
 *
 * This file seeks to demonstrate common strategies used
 * in competitive programming contents.  It's important
 * to note that unlike traditional software engineering
 * we value speedy implementations over well-documented
 * and environmentally conscious solutions.
 *
 * Competitive programming is to programming what NASCAR
 * is to car engineering.
 * 
 *	The gcc compile command is
 *	g++ -std=c++11 -O2 -Wall <file> -o <name>
 *
 **/

// Frequent typedef macros:
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

// Personally I recommend avoiding "#define"s since
// the last thing you want to do is spend time debugging
// marco statements.
// I also recommend using
#include <cstdint>
// for the int type definitions (int64_t) will make
// sure that if you're some strange comp. machine
// you're types will remain somewhat reliable.

int main(int argc, char** argv) {
	// IO is a bottleneck, this lines make it faster.
	ios::sync_with_stdio(0);
	cin.tie(0);

	// for input managed with files we load them into
	// the standard streams
	// freopen("file.txt", "r", stdin);
	// freopen("ouput.txt", "w", stdout);

	// for large integers use long long
	ll really_super_big = 4234729834120392734LL;
	// Note: we use \n over endl since endl flushes
	// the stdout buffer (slow!)
	// cout << really_super_big << '\n';

	// long long is normally just 64 bits but some platforms
	// provide __int128_t for 128 bit integers (possibly useful)	
	// cout << sizeof(long long) << '\n';
	// cout << sizeof(__int128_t) << '\n';

	// Modular arithmetic %!
	// While in formal mathematics modulo cannot be negative, in C++
	// it can!  The modulo returns the "remainder" from a divison operation.
	// To deal with negative remainders we can do the following:
	// x = x % m; 
	// if (x < 0) x += m;

	// FLOATING POINT NUMBERS
	// Floats are the worst.
	// Typically we have the following types:
	// float - 32 bits
	// double - 64 bits
	// long double - 80 bits (g++ extension)

	
	/*
	 * MATHEMATICS
	 *
	 * Being proficient in mathematics (particularly discrete math)
	 * is an essential skill for good competitive programmers.
	 *
	 * Common Formulas:
	 * 	Every sum of the form:
	 *
	 * 	1^k + 2^k + 3^k + ... + n^k has a closed form.
	 *
	 * 	For instance, sum formulas:
	 *
	 *	k=1 : 1 + 2 + 3 ... + n     = (n(n+1))/2
	 *	k=2 : 1 + 4 + 9 + ... + n^2 = (n(n+1)(2n+1))/6
	 *
	 * Just fucking google it I mean god's sake who gives a shit
	 * about memorizing this garbage.
	 **/

	// C++ Data structures
	// Dynamic arrays exist in vectors
	// array here is initialized to 10 items with the
	// value of 5 for each item.
	vector<int> array (10, 5);
	array.push_back(34);
	array.push_back(35);
	/*
	for (auto num : array) {
		printf("%d\n", num);
	}
	*/
	// array.back() // returns last entered element
	array.pop_back(); // removes last element
	
	// C++ Strings Crash-course
	string country = "Haiti"; 
	string countycountry = country + country; // "HaitiHaiti"
	country[2] = 'I';
	// substr(k, x) returns substring starting at index k of size x
	// cout << country.substr(1, 4) << '\n'; // "aIti"
	// find(t) finds the position of the first occurence of a
	// substring t.


	// Set data strucutre (unordered collection of elements)
	// repitition doesn't get taken into account
	// .count will return 1 or 0
	// set --> balanced binary tree O(log n) operations
	// unordered_set --> hashing O(1) operations
	//
	//set<int> s = {2, 3, 3, 9};
	//s.insert(2); s.insert(3); s.insert(3);	
	// cout << s.count(3) << '\n'; // 1
	//s.erase(3);
	// cout << s.count(3) << '\n'; // 0
	// for a set to keep track of the occurences
	// multiset && unordered_multiset should be used.
	typedef unordered_multiset<int> bag;
	bag numbs = {2, 2, 2};
	cout << numbs.count(2) << '\n'; // 3
	numbs.erase(numbs.find(2));	
	cout << numbs.count(2) << '\n'; // 2
	
	// Map structure
	// dictionary data-structures
	// map --> balance binary-tree O(log n) operations
	// unordered_map --> hash table O(1) operations	

	typedef unordered_map<string, int> dict;
	
	dict phone_numbers;
	phone_numbers["Milan"] = 555555555;
	phone_numbers["Yeehaw"] = 1111111111;
	cout << phone_numbers["Milan"] << '\n'; // 555555555
	cout << phone_numbers.count("Milan") << '\n'; // 1

	for (auto entry : phone_numbers) {
		cout << entry.first << " " << entry.second << '\n';
	}


	/* Iterators & Ranges
	 *
	 *	collection.begin() <-- iterator to first element
	 *	collection.end()   <-- iterator to last element
	 *
	 * Many standard library functions rely on iterator interfaces.
	 * For example:
	 * 	sort(v.begin(), v.end());
	 * 	reverse(v.begin(), v.end());
	 *	random_shuffle(v.begin(), v.end());
	 * 
	 * Note: these functions may also work with a regular array
	 * 
	 * sort(a, a+n); // a is a pointer, n is the number of elements
	 *
	 **/
	/*
	 * Iterator interface example below
	auto it = numbs.begin();
        while (it != numbs.end()){
		cout << *it << '\n';
		it++;
	}*/	

	
	auto it = numbs.find(3);
	// normally find returns an iterator,
	// but if it finds nothing it will return the end iterator
	if (it == numbs.end()) {
		cout << "We could not find it ;-;" << '\n';
	}


	// for ordered map & set the methods lower_bound & upper_bound
	// lower_bound(x) --> iterator referencing smallest number larger than x
	// upper_bound(x) --> iterator referencing largest number smaller than x


	/* Misc C++ features that are relevant.
	 * */

	// bitset is a static array where each value is either 0 or 1
	// they are more space efficient than standard arrays
	//bitset<10> s(string("0011011011")); // read from right to left
	//cout << s[0] << '\n';	
	
	// s.count returns the number of 1s in the set.

	// DEQUES ALSO EXIST (GOOD FOR QUEUES)
	deque<int> d;
	d.push_back(5);
	d.push_back(4);
	d.push_front(-2);
	// [-2, 5, 4]
	// pop_back && pop_front are methods which do what you expect

	// STACKS ALSO EXIST
	
	stack<int> s;
	s.push(3);
	s.push(9);
	s.push(18);
	// s.top() returns top value without removing it.
	cout << s.top() << '\n'; // 18

	// queues also legit exist
	queue<int> q;
	q.push(3);
	q.push(9);
	q.push(18);
	// q.front() returns front value without removing it
	q.pop();
	cout << q.front() << '\n';


	// Also, priority queues exist in the STL.
	// yep.  idk why either.

	return 0;
}



