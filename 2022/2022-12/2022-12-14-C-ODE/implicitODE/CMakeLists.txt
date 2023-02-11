add_executable (implicitODE "implicitODE.c"  "vector.h" "vector.c" "quadrate_interp.c" "utils.h" "runge_kutta.c" "simpson.c")

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET implicitODE PROPERTY C_STANDARD 11)
endif()
