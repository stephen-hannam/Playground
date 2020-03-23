BIN = ravg avg_svc _ravg.so
GEN = avg_clnt.c avg_svc.c avg_xdr.c avg.h
RPCCOM = rpcgen
IFLAGS = -I/usr/include/tirpc
LFLAGS = -ltirpc

all: $(BIN)

_ravg.so: _ravg.c avg_clnt.c avg_xdr.c avg.h
	cc -shared -o _ravg.so -fPIC _ravg.c avg_clnt.c avg_xdr.c avg.h $(IFLAGS)

ravg: ravg.o avg_clnt.o avg_xdr.o
	$(CC) -o ravg ravg.o avg_clnt.o avg_xdr.o $(LFLAGS)

avg_svc: avg_proc.o avg_svc.o avg_xdr.o
	$(CC) -o avg_svc avg_proc.o avg_svc.o avg_xdr.o $(LFLAGS)

ravg.o: ravg.c avg.h
	$(CC) ravg.c avg.h -c $(LFLAGS)

_ravg.o: _ravg.c avg.h
	$(CC) _ravg.c avg.h -c $(LFLAGS)

avg_proc.o: avg_proc.c avg.h
	$(CC) avg_proc.c avg.h -c $(LFLAGS)

avg_svc.o: avg_svc.c avg.h
	$(CC) avg_svc.c avg.h -c $(LFLAGS)

avg_clnt.o: avg_clnt.c avg.h
	$(CC) avg_clnt.c avg.h -c $(LFLAGS)

avg_xdr.o: avg_xdr.c avg.h
	$(CC) avg_xdr.c avg.h -c $(LFLAGS)

$(GEN): avg.x
	$(RPCCOM) avg.x

clean cleanup:
	rm -f $(GEN) *.o $(BIN)
	rm -f avg.h.gch
