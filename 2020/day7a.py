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
        m.group(1) for m in re.finditer(r" \d+ ([A-Za-z ]+?) bag(?:s?)[,.]", rule)
    ]
    bag_contents[first_bag] = sub_bags

available_options = ["shiny gold"]
final_options = set()
while available_options:
    bag_poss = available_options.pop()
    for bag in bag_contents:
        if bag_poss in bag_contents[bag]:
            final_options.add(bag)
            available_options.append(bag)

print(len(final_options))
