# $ awk -f awk_column_math.awk emp.data emp.data2

$3 > 0 { print $1, $2 * $3 }
