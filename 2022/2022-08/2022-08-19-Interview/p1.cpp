#include <iostream>
#include <algorithm>
#include <vector>

int arrangements(size_t iN) {
    size_t res = 1; // at least contains [1,2,3,4,..] 

    std::vector<size_t> candidate(iN, 0);
    for (size_t i = 1; i <= iN; i++) { // init
        candidate[i - 1] = i;
    }

    static auto judge = [](size_t iN, const std::vector<size_t> &iVec) -> bool
    {
        for (size_t i = 1; i <= iN; i++)
        {
            if ((iVec[i - 1] % i) && !(i % iVec[i - 1]))
                return false;
        }
        return true;
    };

    while (std::next_permutation(candidate.begin(), candidate.end())) {
        if (judge(iN, candidate)) {
            res ++;
        }
    }
    return res;
}

int main (int argc, char** argv) {
    auto res = arrangements(2);
    return 0;
}