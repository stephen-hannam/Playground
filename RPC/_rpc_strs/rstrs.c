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
    input_data * data;

    if (argc < 2)
    {
        fprintf(stderr, "usage: %s hostname <char *s>\n", argv[0]);
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
    data = (input_data *) malloc(sizeof(input_data));
    data->num_strs = num_strs;

    for (i = 0; i < 5; i++)
    {
        data->argv[i] = (char *) malloc(16*sizeof(char));
        memset(data->argv[i], 0, sizeof(data->argv[i]));
    }

    for (i = 0; i < num_strs; i++)
    {
        data->argv[i] = argv[i+2];
    }

    if ( (sresult = upper_1(data, cl)) == NULL)
    {
        clnt_perror(cl, server);
        exit(3);
    }
    printf("%s\n", *sresult);

    /* data->argv gets freed by xdr routines - but not allocated for some reason */
    free(data);
    clnt_destroy(cl); /* done with the handle */
    exit(0);
}
