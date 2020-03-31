.PHONY: all

all: cli_define_passing

cli_define_passing: cli_define_passing.c
	gcc -o $@ $^

cli_define_passing.c: _cli_define_passing.c
	gcc -E -DPRT=\"hello\" -DPREFIX=hello -DSUFFIX=_1 -P _cli_define_passing.c > cli_define_passing.c
