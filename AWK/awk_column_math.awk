#!/bin/awk -f

# $ awk -f awk_column_math.awk emp.data emp.data2

#$3 > 0 { print $1, $2 * $3 }

# Interesting behaviour here !!!
# The output from this below, will be like
# X made $(N+50)
# X made more than $50
# Y made $M
# etc

# NOT:
# X made $(N+50)
# Y made $M
# X made more than $50

# IE: awk will run all this script to the end at each line,
# not each line of the script for all lines of data before the next line of script

$3 > 0 {printf("%-8s made $%6.2f\n", $1, $2*$3)}
$2 * $3 > 50 {printf("%s made more than $50\n", $1)}
