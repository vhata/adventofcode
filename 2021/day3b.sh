#!/opt/homebrew/bin/bash

INPFILE=day3.txt
TMPD=$(mktemp -d)
cp "$INPFILE" "$TMPD/oday3s1.txt"
cp "$INPFILE" "$TMPD/cday3s1.txt"
len="$(($(head -n1 $INPFILE | wc -c) - 1))"
pushd "$TMPD" > /dev/null
echo -n '^' > opatfile
echo -n '^' > cpatfile
for z in $(seq 1 $len) ; do
    owanted=$(cat oday3s${z}.txt | cut -c${z} | sort | uniq -c | sort -n | tail -n1 | awk '{print $2}')
    cwanted=$(cat cday3s${z}.txt | cut -c${z} | sort | uniq -c | sort -rn | tail -n1 | awk '{print $2}')
    echo -n "$owanted" >> opatfile
    echo -n "$cwanted" >> cpatfile
    egrep -f opatfile oday3s${z}.txt > oday3s$(($z + 1)).txt
    egrep -f cpatfile cday3s${z}.txt > cday3s$(($z + 1)).txt
done

ofile="oday3s$(($z+1)).txt"
cfile="cday3s$(($z+1)).txt"
printf "ibase=2\n$(cat $ofile) * $(cat $cfile)\n" | bc -l
popd > /dev/null
