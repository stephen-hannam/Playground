#!/bin/bash

on='\x1b(0' # Esc ( 0
off='\x1b(B' # Esc ( B

for i in 6a 6b 6c 6d 6e 71 74 75 76 77 78; do
	printf "0x$i \x$i $on\x$i$off\n"
done
