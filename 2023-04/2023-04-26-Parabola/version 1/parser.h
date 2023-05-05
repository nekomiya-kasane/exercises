#ifndef PARSER_H
#define PARSER_H

#include "parabola.h"

class Parser
{
  public:
    Parser(){};

    bool parse(const char *path);

    inline const std::vector<PointVector> &get_data() const { return _data; }

  protected:
    std::vector<PointVector> _data;
};

#endif