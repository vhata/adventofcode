#!/usr/bin/env python

import sys

print(
    sum(
        [
            len(
                list(
                    filter(
                        lambda l: l in (2, 3, 4, 7),
                        [len(c) for c in r.split("|")[1].strip().split()],
                    )
                )
            )
            for r in sys.stdin
        ]
    )
)
