/*
        Prompt: child is running up a staircase with n steps and can hop either 1, 2, or 3
        steps at a time.  Implement a method to count how many possibly ways the child could
        run up the stairs.
*/

#include <bits/stdc++.h>
#include <cstdint>
using namespace std;

typedef int64_t ll;
typedef int32_t num;
typedef __int128_t big;

ll r_steps(ll n)
{
    if (n == 3){
        // 3: 1 1 1, 2 1, 1 2, 3
        return 4;
    } else if (n < 3){
        // 2 : 2, 1 1
        // 1: 1
        return n;
    }
    // if n > 3
    return 3 + r_steps(n-1) + r_steps(n-2) + r_steps(n-3);
}
// Now memoize
ll steps(ll n){
    vector<ll> possible_steps (n, 0);
    possible_steps[0] = 1;
    possible_steps[1] = 2;
    possible_steps[2] = 4;
    for (long unsigned int step = 3; step < possible_steps.size(); step++){
        possible_steps[step] = 3 + possible_steps[step-1] + possible_steps[step-2] + possible_steps[step-3];
    }
    return possible_steps[n-1];
}

int main(int argc, char **argv)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll s;
    cin >> s;
    cout << steps(s) << " possible steps\n";

    // freopen("file.txt", "r", stdin);
    // freopen("ouput.txt", "w", stdout);

    return 0;
}
