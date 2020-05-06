#include <stdio.h>

typedef struct {
  int val;
} ret_t;

ret_t * afunc(void)
{
  ret_t * ret;
  return (ret_t *) 0;
}

int main(int argc, char ** argv)
{
  //ret_t * ret1;

  if ((ret_t * ret1 = afunc()) == NULL)
    printf("yep1\n");

  return 0;
}
