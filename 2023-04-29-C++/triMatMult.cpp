
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char *argv[]) {
  std::vector<std::string> args(argv + 1, argv + argc);

  std::fstream fA(args[0], std::ios::in);
  std::fstream fB(args[1], std::ios::in);

  size_t nA = 0, nB = 0;

  std::vector<int> A;
  std::vector<int> B;

  fA >> nA;
  fB >> nB;

  A.resize(nA * (1 + nA) / 2);
  B.resize(nB * (1 + nB) / 2);

  auto id = [nA](size_t ini, size_t inj) -> size_t {
    int i = static_cast<int>(ini);
    int j = static_cast<int>(inj);
    int a = static_cast<int>(nA);
    int res = -i + j - i * (-1 + i - 2 * a) / 2;
    return static_cast<size_t>(res);
  };

  for (size_t i = 0; i < nA * (1 + nA) / 2; ++i) {
    fA >> A[i];
  }

  for (size_t i = 0; i < nA * (1 + nA) / 2; ++i) {
    fB >> B[i];
  }

  std::vector<int> res;
  res.resize((nA + 1) * nA / 2, 0);
  for (size_t i = 0; i < nA; ++i) {
    for (size_t j = i; j < nA; ++j) {
      for (size_t k = 0; k < nA; ++k) {
        if (j >= i && k >= i && j >= k)
          res[id(i, j)] += A[id(i, k)] * B[id(k, j)];
      }
    }
  }

  for (auto e : res) {
    std::cout << e << " ";
  }
  return 0;
}