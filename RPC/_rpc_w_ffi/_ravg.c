#include "avg.h"
#include <stdlib.h>

int lens[5] = {6,10,6,5,4};

const char *host = "localhost";
const char * _argv[5] = {"_main","localhost","12456","1255","126"};

typedef struct {
  int retcode;
  char * msg;
} ret_t;

double averageprog_1(  char* host, int argc,  char *argv[])
{
  printf("host: %s\n", host);
  for(int i = 0; i < argc; i++)
  {
    printf("%d: ", i);
    for (int j = 0; j < lens[i]; j++)
    {
      printf("%02X ", argv[i][j]);
    }
    printf("\n");
  }

  CLIENT *clnt;
  double  *result_1, *dp, f;
  char *endptr;
  int i;
  input_data  average_1_arg;
  average_1_arg.input_data.input_data_val = (double*) malloc(MAXAVGSIZE*sizeof(double));
  dp = average_1_arg.input_data.input_data_val;
  average_1_arg.input_data.input_data_len = argc - 2;
   for (i=1;i<=(argc - 2);i++)
   {
     f = strtod(argv[i+1],&endptr);
     printf("--value   = %e\n",f);
     *dp = f;
     dp++;
   }
  clnt = clnt_create(host, AVERAGEPROG, AVERAGEVERS, "udp");
  if (clnt == NULL)
  {
     clnt_pcreateerror(host);
     exit(1);
  }
  result_1 = average_1(&average_1_arg, clnt);
  if (result_1 == NULL) {
     clnt_perror(clnt, "call failed:");
  }
  clnt_destroy( clnt );
  //printf("average = %e\n",*result_1);
  return(*result_1);
}

// 6 10 6 5 4

ret_t _main(int argc, char* argv[])
{
  char * host;
  char * str = "hello bitches";
  ret_t ret;
  int retcode = 3;
  for(int i = 0; i < argc; i++)
  {
    printf("%d: ", i);
    for (int j = 0; j < lens[i]; j++)
    {
      printf("%02X ", argv[i][j]);
    }
    printf("\n");
  }

   if(argc < 3)
   {
     printf("usage: %s server_host value ...\n",argv[0]);
     exit(1);
   }
   if(argc > MAXAVGSIZE + 2)
   {
     printf("Two many input values\n");
     exit(2);
   }
   host = argv[1];

   averageprog_1( host, argc, argv);
   //printf("%f\n", ret);
   ret.retcode = retcode;
   ret.msg = str;
   return ret;
}
