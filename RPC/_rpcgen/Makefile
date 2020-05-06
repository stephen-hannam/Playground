BIN = ravg avg_svc
GEN = avg_clnt.c avg_svc.c avg_xdr.c avg.h
RPCCOM = rpcgen

all: $(BIN)

ravg: ravg.o avg_clnt.o avg_xdr.o
	$(CC) -o ravg ravg.o avg_clnt.o avg_xdr.o

avg_svc: avg_proc.o avg_svc.o avg_xdr.o
	$(CC) -o avg_svc avg_proc.o avg_svc.o avg_xdr.o

ravg.o: ravg.c avg.h
	$(CC) ravg.c -c

avg_proc.o: avg_proc.c avg.h
	$(CC) avg_proc.c avg.h -c

avg_svc.o: avg_svc.c avg.h
	$(CC) avg_svc.c avg.h -c

avg_clnt.o: avg_clnt.c avg.h
	$(CC) avg_clnt.c avg.h -c

avg_xdr.o: avg_xdr.c avg.h
	$(CC) avg_xdr.c avg.h -c

$(GEN): avg.x
	$(RPCCOM) avg.x

clean cleanup:
	rm -f $(GEN)* *.o $(BIN)
