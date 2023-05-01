Dict={
      "S":["aA","dE"],
      "A":["aB","aS"],
      "B":["bC"],
      "C":["bD","bB"],
      "D":["cD","$"],
      "E":["$"]
      }

cuv=[]
for litera in Dict["S"]:
    cuv.append(litera)
print(cuv)
n=int(input("n="))
for i in range(n-1):
    cuv2=[]
    for litera in cuv:
        if litera[-1] != "$":
            for litera2 in Dict[litera[-1]]:
                 cuv2.append(litera[:-1]+litera2)
    cuv=cuv2
final=[]
for chei in Dict:
    if "$" in Dict[chei]:
        final.append(chei)
print(final)

for litera in cuv:
    if litera[-1] in final:
        print(litera[:-1])
