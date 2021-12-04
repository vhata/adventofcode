#!/usr/bin/env python

import re
import sys

bag_contents = {}

# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
first_bag = re.compile(
    r"^([A-Za-z ]+?) bags contain( \d+ ([A-Za-z ]+?) bag(?:s?)[,.])+$"
)

for rule in map(str.strip, sys.stdin):
    first_bag_m = re.match(r"^([A-Za-z ]+?) bags contain", rule)
    assert first_bag_m
    first_bag = first_bag_m.group(1)
    sub_bags = [
        (int(m.group(1)), m.group(2))
        for m in re.finditer(r" (\d+) ([A-Za-z ]+?) bag(?:s?)[,.]", rule)
    ]
    bag_contents[first_bag] = sub_bags


def bags_inside(bag_col: str, level=0) -> int:
    count = 0
    for c, bag in bag_contents[bag_col]:
        count = count + (c * (1 + bags_inside(bag, level + 1)))
    return count


print(bags_inside("shiny gold"))
