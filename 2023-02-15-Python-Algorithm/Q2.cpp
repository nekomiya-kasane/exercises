#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>

using namespace std;

const int M = 100001;
int d[M];
int n, k;
queue<int> q;

int bfs() {
  memset(d, -1, sizeof(d));
  d[n] = 0;

  q.push(n);

  while (!q.empty()) {
    auto t = q.front();
    q.pop();

    for (auto offset : {1, -1}) {
      auto x = t + offset;
      if (x >= 0 && x < M && d[x] == -1) {
        d[x] = d[t] + 1;
        q.push(x);
      }
      if (x == k)
        return d[k];
    }

    auto x = t * 2;
    if (x >= 0 && x < M && d[x] == -1) {
      d[x] = d[t] + 1;
      q.push(x);
    }
    if (x == k)
      return d[k];
  }
  return d[k];
}

int main() {
  cin >> n >> k;
  cout << bfs() << endl;
  return 0;
}