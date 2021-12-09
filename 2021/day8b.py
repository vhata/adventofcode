#!/usr/bin/env python

import sys

# 2: 1
# 3: 7
# 4: 4
# 5: 2, 3, 5
# 6: 0, 6, 9
# 7: 8

count = 0
for r in map(str.strip, sys.stdin):
    inputs, outputs = map(str.split, map(str.strip, r.split("|")))
    inputs = ["".join(sorted(s)) for s in inputs]
    outputs = ["".join(sorted(s)) for s in outputs]
    digits = {}
    coll = lambda l: [i for i in inputs if len(i) == l]
    d_one = coll(2)[0]
    d_four = coll(4)[0]
    d_seven = coll(3)[0]
    d_eight = coll(7)[0]

    d_six = [i for i in coll(6) if not set(i).issuperset(set(d_one))][0]
    d_five = [i for i in coll(5) if set(i).issubset(set(d_six))][0]
    d_nine = [i for i in coll(6) if i != d_six and set(i).issuperset(set(d_five))][0]
    d_three = [i for i in coll(5) if i != d_five and set(i).issubset(set(d_nine))][0]
    d_zero = (set(coll(6)) - set([d_six, d_nine])).pop()
    d_two = (set(coll(5)) - set([d_five, d_three])).pop()

    digits[d_zero] = 0
    digits[d_one] = 1
    digits[d_two] = 2
    digits[d_three] = 3
    digits[d_four] = 4
    digits[d_five] = 5
    digits[d_six] = 6
    digits[d_seven] = 7
    digits[d_eight] = 8
    digits[d_nine] = 9
    val = 0
    for o in outputs:
        val = (val * 10) + digits[o]
    count = count + val

print(count)
