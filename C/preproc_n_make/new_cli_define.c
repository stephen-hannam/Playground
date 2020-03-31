#include "cli_define_passing.c"

#define STR(x) x
#define TOKENPASTE(x, y) x ## y
#define TOKENPASTE2(x, y) TOKENPASTE(x, y)

#ifndef PREFIX
#define PREFIX Main_
#endif

#ifndef SUFFIX
#define
#define SUFFIX __LINE__
#endif

#define FUNC TOKENPASTE2(PREFIX, SUFFIX)

int _main(int argc, char ** argv){
  FUNC(argc, argv);
  return 0;
}
