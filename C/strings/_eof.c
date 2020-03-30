#include <stdio.h>

int main(int argc, char ** argv)
{
  char str[6];
  sprintf(str, "%d", EOF);
  printf("%s\n", str);
  printf("%c\n", EOF);
  printf("%4c\n", EOF);
  printf("%8c\n", EOF);
  printf("%8X\n", EOF);
  printf("%010X\n", EOF);
  printf("%c\n", 0x02);
  printf("%c\n", 0x03);

  FILE * stream;
  size_t size;
  char * _str;

  printf("\n");
  printf("hello\n");

  stream = open_memstream(&_str, &size);
  fprintf(stream, "%c\n", 0x02);
  fprintf(stream, "%s", "hello\n");
  fprintf(stream, "%c\n", 0x03);
  fprintf(stream, "%d", 0);
  fflush(stream);
  fclose(stream);
  printf("%s", _str);

  return 0;
}
