#include <stdio.h>
#include <string.h>

int _main(int argc, char * argv[]){
  printf("hello world\n");
  printf("hello %s\n", argv[0]);
  printf("hello %s", argv[1]);
  return 0;
}
