# flag : 4729a4a6bbdd4d78c94e6229257af35e

import byte_analizer as ba

with open("bcode.lbc", "r") as fi:
  statmts = fi.read().split("\n")
  for i in statmts:
    ba.analize(string = i)