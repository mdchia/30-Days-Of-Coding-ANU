#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int tribonacci(int n){
    n++;
    int i0=0;
    int i1=0;
    int i2=1;
    int i3=1;
    switch(n){
        case 1: return i2;
        case 2: return i2;
        case 3: return i2;
    }
    for(int ix = 0; ix < n-1; ix++){
        i3=i2+i1+i0;
        i0=i1;
        i1=i2;
        i2=i3;
    }
    return i2;
}


int main(){
    int s;
    cin >> s;
    for(int a0 = 0; a0 < s; a0++){
        int n;
        cin >> n;
        cout << tribonacci(n) << endl;
    }
    return 0;
}
