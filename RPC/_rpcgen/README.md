## Beginners walk-thru using rpcgen

online resources:

1. https://www.linuxjournal.com/article/2204

### pkg: install whatever provides rpcinfo (usu. rpcbind)

eg: `$ sudo apt install rpcbind`

also add line `avg        22855` to `/etc/rpc`

some distros may have deprecated SunRPC in glibc: eg, Fedora >= 28

eg: on Fedora `$ dnf install libtirpc.x86_64 libtirpc-devel.x86_64`

NB: service may require manually start

### rpcgen: the protocol compiler

`$ rpcgen avg.x` produces `avg.h`, `avg_clnt.c`, `avg_svc.c`, and `avg_xdr.c`

see `Makefile` for full recipe

## Run the demo

`$ ./avg_svc &` for the server

`$ rpcinfo -p localhost` to query service status

`$ ./ravg localhost $RANDOM $RANDOM $RANDOM` to run client
