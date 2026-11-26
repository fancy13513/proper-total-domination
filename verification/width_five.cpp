// g++ -std=c++17 -O3 width_five.cpp -o width_five
// Use each legal triple of five-bit columns as a state. Arc cost is the
// number of selected vertices in the middle column of its source state.
#include <algorithm>
#include <array>
#include <iostream>
#include <vector>
using namespace std;
constexpr int rows = 5, masks = 1 << rows, inf = 1000000;
constexpr int base_length = 48;
struct State {
    int left, middle, right, weight;
    array<int, rows> score;
};
struct Arc { int from, to; };
int bit(int col, int i) { return (col >> i) & 1; }

int main() {
    vector<State> states;
    array<vector<int>, masks*masks> prefixes;
    for (int a=0; a<masks; ++a) for (int b=0; b<masks; ++b) for (int c=0; c<masks; ++c) {
        State t{a,b,c,0,{}};
        for (int j=0; j<rows; ++j) {
            t.weight += bit(b,j);
            t.score[j] = bit(a,j) + bit(c,j) + bit(b,(j+1)%rows) + bit(b,(j+rows-1)%rows);
        }
        bool good = true;
        for (int j=0; j<rows; ++j)
            if (!t.score[j] || t.score[j] == t.score[(j+1)%rows]) good = false;
        if (good) {
            prefixes[a*masks+b].push_back(static_cast<int>(states.size()));
            states.push_back(t);
        }
    }
    vector<Arc> arcs;
    int n = static_cast<int>(states.size());
    for (int i=0; i<n; ++i) {
        const State& u=states[i];
        for (int v : prefixes[u.middle*masks+u.right]) {
            bool good=true;
            for (int j=0; j<rows; ++j)
                if (u.score[j] == states[v].score[j]) good=false;
            if (good) arcs.push_back({i,v});
        }
    }
    cout << "states " << n << ", arcs " << arcs.size() << '\n';
    vector<int> diagonal(base_length+3,inf);
    vector<int> previous(n),next(n),saved(n),cost(n);
    long long compared=0,finite=0;
    for (int origin=0; origin<n; ++origin) {
        fill(previous.begin(),previous.end(),inf);
        previous[origin]=0;
        for (int t=1; t<=base_length+2; ++t) {
            for (int i=0; i<n; ++i) cost[i]=previous[i]+states[i].weight;
            fill(next.begin(),next.end(),inf);
            for (auto e : arcs) next[e.to]=min(next[e.to],cost[e.from]);
            previous.swap(next);
            diagonal[t]=min(diagonal[t],previous[origin]);
            if (t == base_length) saved=previous;
        }
        for (int i=0; i<n; ++i) {
            int want=(saved[i]==inf ? inf : saved[i]+5);
            if (previous[i]!=want) {
                cerr << "Recurrence fails for ordered pair " << origin << ' ' << i << '\n';
                return 1;
            }
            ++compared;
            if (saved[i]!=inf) ++finite;
        }
    }
    cout << "D[" << base_length+2 << "] = D[" << base_length
         << "] + 5 checked on " << compared << " ordered pairs, " << finite << " finite\n";
    for (int t=3;t<=base_length+2;++t) {
        cout << t << ' ';
        if (diagonal[t]==inf) cout << "infinity"; else cout << diagonal[t];
        cout << '\n';
    }
}
