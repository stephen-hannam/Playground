BIN=strs_svc rstrs
GEN=strs_clnt.c strs_svc.c strs.h strs_xdr.c
RPC=rpcgen

.PHONY: clean
.PHONY: all

all: $(BIN)

strs_svc: strs_svc.o strs_proc.o strs_xdr.o
	$(CC) -o $@ $^

rstrs: rstrs.o strs_clnt.o strs_xdr.o
	$(CC) -o $@ $^

strs_xdr.o: strs_xdr.c strs.h
	$(CC) -c $^

strs_svc.o: strs_svc.c strs.h
	$(CC) -c $^ -DRPC_SVC_FG

strs_clnt.o: strs_clnt.c strs.h
	$(CC) -c $^

strs_proc.o: strs_proc.c strs.h
	$(CC) -c $^

rstrs.o: rstrs.c strs.h
	$(CC) -c $^

$(GEN): strs.x
	$(RPC) $^


clean:
	rm -f $(GEN) $(BIN) *.h* *.o
