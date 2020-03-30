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

#define DEP1 <stdio.h>
#define DEP2 <string.h>

#define INC1 #include TOKENPASTE2(DEP1,)
#define INC2 #include TOKENPASTE2(DEP2,)

INC1
INC2

int FUNC()
{
#ifdef PRT
  printf("%s", STR(PRT));
#else
#error "must provide -DPRT=\"value\" in compile options"
#endif
  return 0;
}

int main(int argc, char ** argv){
  FUNC();
  return 0;
}
