#!/usr/bin/env python3.8

from functools import reduce
from itertools import islice
import sys

monkey_info = {}
monkeys = []
while r := list(islice(sys.stdin, 7)):
    monkey = {}
    _, monkey_num = r[0].strip().strip(":").split()
    monkeys.append(monkey_num)

    _, _, items_s = r[1].strip().split(None, 2)
    monkey["items"] = list(map(int, items_s.split(", ")))
    monkey["operation"] = r[2].strip()[len("Operation: new = ") :]
    monkey["divis"] = int(r[3].strip().split()[3])  # all tests are "is divisible by"
    monkey["recips"] = tuple(r[x].strip().split()[-1] for x in [4, 5])
    monkey["inspections"] = 0

    monkey_info[monkey_num] = monkey

for _ in range(20):
    for mn in monkeys:
        m = monkey_info[mn]
        for item in m["items"]:
            m["inspections"] += 1
            item = eval(m["operation"], {"old": item})
            item = item // 3
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
