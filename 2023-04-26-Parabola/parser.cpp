
#include <fstream>
#include <regex>
#include <string>

#include "parser.h"

Point Point::origin = {0, 0}; 

bool Parser::parse(const char *path)
{
    std::fstream file;
    file.exceptions(file.exceptions() | std::ios::failbit);

    try {
        file.open(path);
    }
    catch (std::exception& e) {
        std::cout << e.what() << '\n';
    }

    if (!file.is_open())
        return false;

    std::regex re("(.),(\\d+),-?(\\d+)");

    std::string line;
    std::smatch cm;

    size_t lino = 0;
    
    while (!file.eof() && std::getline(file, line))
    {
        lino ++;
        bool match = std::regex_search(line, cm, re);
        if (cm.empty() || cm[1] == "p" && cm.size() <= 3) // expected 4
        {
            TRACE("Bad line: " + line);
            continue;
        }
        else if (cm[1] == "#")
        {
            if (_data.empty() || _data.back().size() > 2)
                _data.emplace_back();
        }
        else if (cm[1] == "p")
        {
            Point pt = {std::stod(cm[2]), std::stod(cm[3])};
            _data.back().push_back(pt);
        }
        else {
            break;
        }
    }

    if (_data.back().size() < 2)
        _data.pop_back();

    if (_data.empty())
        return false;

    return true;
}