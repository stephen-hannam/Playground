#!/bin/awk -f

# $ ./parse_groceries.awk shopping_list.csv
# can also run: awk -f parse_groceries.awk shopping_list

# /produce/ {print $2}

#BEGIN {print "Produce to pick up from the store:"}
#/produce/ {print $2}
#END {print "--------------"}

#BEGIN {  FS=","
#  print "Produce to pick up from the store:"}
#/produce/ {print $2}
#END {print "--------------"}

#BEGIN {  FS=","
#  print "Produce to pick up from the store:"}
#$3>1 {print $2}
#END {print "--------------"}

#BEGIN {  FS=","
#  print "Produce to pick up from the store:"}
#$3>1 {print $2}
#/dairy/ {print $2}
#END {print "--------------"}

BEGIN {  FS=","
  print "Produce to pick up from the store:"}
$3>1 || /dairy/ {print $2}
END {print "--------------"}
