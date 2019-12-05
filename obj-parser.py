from os.path import isfile, isdir, join
from sys import argv
import re
import os


class obj(object):
    def __init__(self, path):
        self.path = path

    def is_maya(self):
        filesObj = []
        filesAll = []

        if isdir(self.path):
            for root, dirs, files in os.path.walk(self.path):
                for item in files:
                    filesAll.append(join(root, item))
            for item in filesAll:
                if item.endswith(".obj"):
                    filesObj.append(item)
            return list(filesObj)

        elif isfile(self.path):
            if self.path.endswith(".obj"):
                return self.path

    def tokenize(self):
        pass


# Token Specification
GEO = re.compile(r"(?P<GEO>([a-zA-Z_0-9]*))")
LIB = re.compile(r"(?P<LIB>(?:(?:mtllib)|(?:adobemdllib)) ([a-zA-Z0-9_]*.(?:mtl)|(?:mdl)))")
USE = re.compile(r"(?P<USE>usemtl ([a-zA-Z_0-9]*))")
TRI = re.compile(r"(?P<USE>usemtl ([a-zA-Z_0-9]*))")

tris = int(0)
quads = int(0)
fiveGons = int(0)
nGons = int(0)


mtl_name = []
with open(argv[1], "rt") as f:
    for line in f:
        f.readline().rstrip()
        u = USE.scanner(line.rstrip()).match()
        t = TRI.scanner(line.rstrip()).match()
        ll = LIB.scanner(line.rstrip()).match()
        g = GEO.scanner(line.rstrip()).match()
        if u:
            print(u)
        elif t:
            tris += 1
        elif g:
            print(g.group(2))
        elif ll:
            mtl_name.append(ll.group(2))
    print(mtl_name)
    print(tris)
    print(tris),
