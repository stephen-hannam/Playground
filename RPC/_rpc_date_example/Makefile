BIN=date_svc rdate
GEN=date_clnt.c date_svc.c date.h #date_xdr.c
RPC=rpcgen

.PHONY: clean
.PHONY: all

all: $(BIN)

date_svc: date_svc.o date_proc.o #date_xdr.o
	$(CC) -o $@ $^

rdate: rdate.o date_clnt.o #date_xdr.o
	$(CC) -o $@ $^

#date_xdr.o: date_xdr.c date.h
#	$(CC) -c $^

date_svc.o: date_svc.c date.h
	$(CC) -c $^ -DRPC_SVC_FG

date_clnt.o: date_clnt.c date.h
	$(CC) -c $^

date_proc.o: date_proc.c date.h
	$(CC) -c $^

rdate.o: rdate.c date.h
	$(CC) -c $^

$(GEN): date.x
	$(RPC) $^


clean:
	rm -f $(GEN) $(BIN) *.h* *.o
