#!/bin/bash

# SIGINT (^C) is Trappable, kill -9 is NOT Trappable
# therefore, signals can be Trappable or Non-Trappable

trap 'alert "Program was interrupted"' SIGINT

alert(){
  echo "*********************"
  echo $1
  echo "*********************"
}

alert "do dee do dee doo dee do"

echo "press any key to continue"
read
echo "bye"
