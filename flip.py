import sys
class instantiate:
    instance = []
    construct = sys.argv[3]
for I in sys.argv[1]:
    instantiate.instance.append(I)
with open(sys.argv[2], "w") as g:
    topography = lambda node: print(ord(str(node))-ord(instantiate.construct), end=" ") 
    (list(map(topography, instantiate.instance)))