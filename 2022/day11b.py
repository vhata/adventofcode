#!/usr/bin/env python3.8

from functools import reduce
from itertools import islice
import sys

monkey_info = {}
monkeys = []

ops = {
    "*": lambda a, b: a * b,
    "+": lambda a, b: a + b,
}
var = lambda x, y: y if x == "old" else int(x)

while r := list(islice(sys.stdin, 7)):
    monkey = {}
    _, monkey_num = r[0].strip().strip(":").split()
    monkeys.append(monkey_num)

    _, _, items_s = r[1].strip().split(None, 2)
    monkey["items"] = list(map(int, items_s.split(", ")))
    monkey["operation"] = r[2].strip()[len("Operation: new = old ") :]
    monkey["divis"] = int(r[3].strip().split()[3])  # all tests are "is divisible by"
    monkey["recips"] = tuple(r[x].strip().split()[-1] for x in [4, 5])
    monkey["inspections"] = 0

    monkey_info[monkey_num] = monkey

# The trick(tm) - if we modulo our worry by all the divisors (which are all prime)
# then the rule about divisibility will stay the same
supermod = reduce(lambda a, b: a * b, [monkey_info[mn]["divis"] for mn in monkeys])

for _ in range(10000):
    for mn in monkeys:
        m = monkey_info[mn]
        for item in m["items"]:
            m["inspections"] += 1
            op = m["operation"]
            item = ops[op[0]](item, var(op[2:], item))
            item = item % supermod
            if not item % m["divis"]:
                recip = m["recips"][0]
            else:
                recip = m["recips"][1]
            monkey_info[recip]["items"].append(item)
        m["items"] = []  # all thrown away

print(
    reduce(
        lambda a, b: a * b, sorted(monkey_info[m]["inspections"] for m in monkeys)[-2:]
    )
)
