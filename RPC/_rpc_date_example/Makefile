BIN=date_svc rdate
GEN=date_clnt.c date_svc.c date.h #date_xdr.c
RPC=rpcgen
IFLAGS=-I/usr/include/tirpc
LFLAGS=-ltirpc

.PHONY: clean
.PHONY: all

all: $(BIN)

date_svc: date_svc.o date_proc.o #date_xdr.o
	$(CC) -o $@ $^ $(LFLAGS)

rdate: rdate.o date_clnt.o #date_xdr.o
	$(CC) -o $@ $^ $(LFLAGS)

#date_xdr.o: date_xdr.c date.h
#	$(CC) -c $^ $(LFLAGS)

date_svc.o: date_svc.c date.h
	$(CC) -c $^ $(IFLAGS) -DRPC_SVC_FG

date_clnt.o: date_clnt.c date.h
	$(CC) -c $^ $(IFLAGS)

date_proc.o: date_proc.c date.h
	$(CC) -c $^ $(IFLAGS)

rdate.o: rdate.c date.h
	$(CC) -c $^ $(IFLAGS)

$(GEN): date.x
	$(RPC) $^


clean:
	rm -f $(GEN) $(BIN) *.h* *.o
