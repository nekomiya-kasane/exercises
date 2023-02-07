#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <functional>

using namespace std;

int maxEvents(vector<int> arrival, vector<int> duration)
{

    std::vector<std::pair<int, int>> intervals(arrival.size());

    for (size_t i = 0; i < arrival.size(); i++)
    { // prepare
        intervals.push_back({arrival[i], arrival[i] + duration[i]});
    }

    std::sort(intervals.begin(), intervals.end(),
              [](const std::pair<int, int> &lt, const std::pair<int, int> &rt) -> bool
              { return lt.second < rt.second; });

    // count
    auto cur = intervals[0].second;
    int res = 1;
    for (size_t i = 1; i < intervals.size(); i++)
    {
        if (intervals[i].first >= cur)
        {
            cur = intervals[i].second;
            res++;
        }
    }
    return res;
}

// tree

int loop(int *table, int *parents, int *weights, int *pats, int node, int N)
{
    for (int j = 0; j < N; j++)
    {
        if (table[node * N + j] > 0)
        {
            weights[node] += loop(table, parents, weights, pats, j, N);
            pats[node] += pats[j];
        }
    }
    return pats[node] / 5 + (int)(pats[node] % 5 != 0) + weights[node];
}

void gen_tree(int *table, int *parents, int *temp, int node, int N)
{
    temp[node] = 1;
    for (int j = 0; j < N; j++)
    {
        if (table[node * N + j] != 0 && !temp[j])
        {
            table[node * N + j] = 1;
            table[j * N + node] = -1;

            parents[j] = node;
            gen_tree(table, parents, temp, j, N);
        }
    }
}

int solution(int A[], int B[], int iN)
{
    // build tree
    int N = iN + 1;

    int *table = (int *)malloc(sizeof(int) * (N * N));
    int *parents = (int *)malloc(sizeof(int) * (N));
    int *weights = (int *)malloc(sizeof(int) * (N));
    int *pats = (int *)malloc(sizeof(int) * (N));
    int *temp = (int *)malloc(sizeof(int) * (N));

    for (int i = 0; i < N * N; i++)
    {
        table[i] = 0; // 0 for not connected
    }

    for (int i = 0; i < N; i++)
    {
        parents[i] = -1; // 0 for not connected
        weights[i] = 0;
        pats[i] = 1;
        temp[i] = 0;
    }

    for (int k = 0; k < N - 1; k++)
    {
        unsigned i = A[k];
        unsigned j = B[k];

        table[i * N + j] = 1;
        table[j * N + i] = -1;

        parents[j] = i;
    }

    gen_tree(table, parents, temp, 0, N);

    // DFS
    loop(table, parents, weights, pats, 0, N);

    free(table);
    free(parents);
    free(weights);
    free(temp);
    free(pats);
    return weights[0];
}

int solution2(vector<int> &A, vector<int> &B)
{
    auto n = A.size() + 1;

    std::vector<std::vector<int>> tree(n);

    // generate tree
    {
        std::map<int, std::vector<int>> graph;

        std::vector<int> visited;

        for (auto i = 0; i < n - 1; i++)
        {
            graph[A[i]].push_back(B[i]);
            graph[B[i]].push_back(A[i]);
        }

        std::function<void(std::vector<std::vector<int>>&, int)> gen_tree;

        gen_tree = [&gen_tree, &graph, &visited](std::vector<std::vector<int>> &otree, int node) -> void
        {
            visited.push_back(node);
            for (const auto connected : graph[node])
            {
                if (std::find(visited.begin(), visited.end(), connected) != visited.end())
                    continue;
                otree[node].push_back(connected);
                gen_tree(otree, connected);
            }
        };

        gen_tree(tree, 0);
    }

    // recursive
    std::function<int(std::vector<std::vector<int>>&, int)> loop;

    std::vector<int> weights(n), pats(n, 1);

    loop = [&loop, &weights, &pats](std::vector<std::vector<int>> &otree, int node) -> int
    {
        for (auto leaf : otree[node])
        {
            weights[node] += loop(otree, leaf);
            pats[node] += pats[leaf];
        }
        return pats[node] / 5 + (int)(pats[node] % 5 != 0) + weights[node];
    };

    loop(tree, 0);

    return weights[0];
}

// end 

int main()
{
    std::vector<int> A = {1,1,1,9,9,9,9,7,8};
    std::vector<int> B = {2,0,3,1,6,5,4,0,0};
    auto res = solution2(A, B);
}