#!/usr/bin/env python

from dataclasses import dataclass
from typing import Dict
import sys

f = open("day21sample.txt")
p1pos = int(f.readline().strip().split()[-1])
p2pos = int(f.readline().strip().split()[-1])


@dataclass
class Player:
    num: int
    score: int
    pos: int


@dataclass
class GameState:
    ps: Dict[str, Player]

    def maxscore(self):
        return max(p.score for p in self.ps.values())

    def maxp(self):
        return [g for g in self.ps if self.ps[g].score == self.maxscore()]

    def id(self):
        g = self
        return "-".join(
            [f"{g.ps[p].num}-{g.ps[p].score}-{g.ps[p].pos}" for p in sorted(g.ps)]
        )


def advance(cur, n):
    cur = cur + n
    while cur > 10:
        cur = cur - 10
    return cur


topscore = 21
scores = [{}] * (topscore + 1)
initgame = GameState({"p1": Player(1, 0, p1pos), "p2": Player(1, 0, p2pos)})
scores[0] = {initgame.id(): initgame}

otherplayer = {"p1": "p2", "p2": "p1"}


def mergescores(a, b):
    newscores = [{} for a in range(topscore + 1)]
    for i in range(topscore + 1):
        ids = set(a[i].keys()).union(set(b[i].keys()))
        for id in ids:
            ascore = a[i].get(id)
            bscore = b[i].get(id)
            if not ascore:
                newscores[i][id] = bscore
            elif not bscore:
                newscores[i][id] = ascore
            else:
                ap1, ap2 = ascore.ps["p1"], ascore.ps["p2"]
                bp1, bp2 = bscore.ps["p1"], bscore.ps["p2"]
                p1 = Player(ap1.num + bp1.num, ap1.score, ap1.pos)
                p2 = Player(ap2.num + bp2.num, ap2.score, ap2.pos)
                newscores[i][id] = GameState({"p1": p1, "p2": p2})
    return newscores


def move(scores, pname, n):
    otherp = otherplayer[pname]

    newscores = [{} for a in range(topscore + 1)]
    for i in range(topscore):
        gs = scores[i]
        for g in gs.values():
            p = g.ps[pname]

            newpos = advance(p.pos, n)
            newscore = p.score + newpos
            # don't overflow scores, won is won
            if newscore > topscore:
                newscore = topscore
            newp = Player(p.num, newscore, newpos)

            newgame = GameState({pname: newp, otherp: g.ps[otherp]})
            exis_g = newscores[newgame.maxscore()].get(newgame.id())
            if exis_g:
                exis_g_maxp = exis_g.ps[exis_g.maxp()]
                newg_maxp = newgame.ps[newgame.maxp()]
                exis_g_maxp.num = exis_g_maxp.num + newg_maxp.num
            else:
                newscores[newgame.maxscore()][newgame.id()] = newgame
    return newscores


"""
    scores = newscores
    for i in range(topscore):
        gs = scores[i]
                upd_sc = scores[newscore]
                if not upd_sc.get(pname):
                    upd_sc[pname] = [Players(p.num, newturns, newpos)]
                else:
                    found = False
                    for scit in range(len(upd_sc[pname])):
                        this_ps = upd_sc[pname][scit]
                        if this_ps.turns == newturns and this_ps.pos == newpos:
                            this_ps.num = this_ps.num + p.num
                            found = True
                    if not found:
                        upd_sc[pname].append(Players(p.num, newturns, newpos))
            del scores[i][pname]
"""


def roll(scores, pname):
    # roll the dice three times, and move their sum
    newscores = [{} for a in range(topscore + 1)]
    for r1 in range(1, 4):
        newsc = move(scores, pname, r1)
        newscores = mergescores(newscores, newsc)
        continue
        for r2 in range(1, 4):
            for r3 in range(1, 4):
                move(pname, r1 + r2 + r3)
    return newscores


import IPython

IPython.embed()
