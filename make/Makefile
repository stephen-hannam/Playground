BIN=hello

DEPDIR=./deps/

$(BIN): $(addprefix $(DEPDIR), hello.c hello1.c hello2.c)
	cc -o $@ $^
