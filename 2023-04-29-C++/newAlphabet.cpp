
#include <iostream>
#include <string>
#include <vector>


size_t sbit = 0b1 << 26;
size_t mask = sbit - 1;

int main(int argc, char *argv[]) {
  if (argc == 1) {
    std::cout << "Param needed." << std::endl;
    return -1;
  }

  std::vector<std::string> args(argv + 1, argv + argc);

  std::string res;

  auto decoder = [](int c) -> char {
    bool capital = c & sbit;
    c &= mask;
    int i = 0;
    for (; i < 26; ++i) {
      if (c >> i == 0)
        break;
    }
    return static_cast<char>((capital ? 'A' : 'a') + i - 1);
  };

  try {
    for (auto arg : args) {
      res.push_back(decoder(std::stoi(arg)));
    }
  } catch (...) {
    std::cout << "Wrong key" << std::endl;
  }

  std::cout << "You entered the word: " << res << std::endl;

  return 0;
}