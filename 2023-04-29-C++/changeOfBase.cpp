#include <iostream>
#include <string>


int main() {
  unsigned curBase = 0, targetBase = 0;

  std::string number;

  std::cout << "Please enter the number's base: ";
  std::cin >> curBase;
  std::cout << "Please enter the numebr: ";
  std::cin >> number;
  std::cout << "Please enter the new base: ";
  std::cin >> targetBase;

  if (curBase < 2 || curBase > 36 || targetBase < 2 || targetBase > 36) {
    std::cout << "Wrong base." << std::endl;
  }

  size_t value = 0;
  size_t turn = 1;
  for (auto it = number.rbegin(); it < number.rend(); it++) {
    int step = 0;
    if (*it >= '0' && *it <= '9')
      step = *it - '0';
    else if (*it >= 'A' && *it <= 'Z')
      step = *it - 'A' + 10;
    else if (*it >= 'a' && *it <= 'z')
      step = *it - 'a' + 10;
    else
      return -2;

    value += step * turn;
    turn *= curBase;
  }

  std::string res;
  while (value) {
    auto digit = static_cast<size_t>(value % targetBase);
    value /= targetBase;

    std::string dig = "0";
    if (digit < 10) {
      dig[0] = static_cast<char>(digit + '0');
    } else {
      dig[0] = static_cast<char>(digit - 10 + 'A');
    }

    res = dig + res;
  }

  std::cout << number << " base " << curBase << " is " << res << " base "
            << targetBase << std::endl;
  return 0;
}