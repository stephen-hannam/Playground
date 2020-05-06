#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int ret = 0;

int cleanup(int val, bool exiting)
{
  static int ret2 = 0;
  if (!exiting)
    ret2 = val;
  else
    return ret2;
}

static void exit_handler(void)
{
  ret = cleanup(0, true);
  printf("exit handler called: ret = %d\n", ret);
  return;
}

void func1(void)
{
  printf("entering func1\n");
  exit(3);
  printf("will I see this?\n");
  return;
}

int main(int argc, char ** argv)
{
  cleanup(2, false);

  if(atexit(exit_handler) != 0)
  {
    printf("atexit failed\n");
  }

  func1();

  printf("after exit handler\n");

  return ret;
}
