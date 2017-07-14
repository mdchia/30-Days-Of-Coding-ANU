read input
for i in `seq 1 10`;
do
    output=$(expr $input \* $i)
    echo $input" x "$i" = "$output
done
