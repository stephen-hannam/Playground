#include <stdio.h>

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

#define FUNC int TOKENPASTE2(PREFIX, SUFFIX)(int argc, char ** argv)

FUNC
{
#ifdef PRT
  printf("%s", STR(PRT));
#else
#error "must provide -DPRT=\"value\" in compile options"
#endif
  return 0;
}
