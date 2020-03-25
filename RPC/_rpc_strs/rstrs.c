/*
* rdate.c  client program for remote date program
*/
#include <stdio.h>
#include <rpc/rpc.h> /* standard RPC include file */
#include "strs.h" /* this file is generated by rpcgen */

int main(int argc, char *argv[])
{
    CLIENT *cl; /* RPC handle */
    char *server;
    char **sresult; /* return value from str_date_1() */
    int i, num_strs;

    if (argc < 2)
    {
        fprintf(stderr, "usage: %s hostname <strings>\n", argv[0]);
        exit(1);
    }
    server = argv[1];
    /*
    * Create client handle
    */
    if ((cl = clnt_create(server, STRS_PROG, STRS_VERS, "tcp")) == NULL)
    {
        /*
        * can’t establish connection with server
        */
        clnt_pcreateerror(server);
        exit(2);
    }

    num_strs = argc - 2;
    for (i = 2; i < num_strs + 2; i++)
    {
      if ( (sresult = upper_1(&argv[i], cl)) == NULL)
      {
          clnt_perror(cl, server);
          exit(3);
      }
      printf("%s\n", *sresult);
    }

    clnt_destroy(cl); /* done with the handle */
    exit(0);
}
