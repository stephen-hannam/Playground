.PHONY: first
.PHONY: second

second: new_cli_define

first: cli_define_passing

new_cli_define: new_cli_define.c cli_define_passing.c
	gcc -E -DPREFIX=Main -DSUFFIX=_1 -P new_cli_define.c > tmp.c
	sed -i -e 's|\bmain\b|Main_1|g' tmp.c
	sed -i -e 's|\b_main\b|main|g' tmp.c
	gcc -o $@ tmp.c
	rm tmp.c


cli_define_passing: cli_define_passing.c
	gcc -o $@ $^

cli_define_passing.c: _cli_define_passing.c
	gcc -E -DPRT=\"hello\" -DPREFIX=hello -DSUFFIX=_1 -P _cli_define_passing.c > cli_define_passing.c
