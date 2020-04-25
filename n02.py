n1 = "パトカー"
n2 = "タクシー"
name = ""
x = 0
y = 0
while x<4 :
    for name1 in (n1[x]):
        x += 1
    for name2 in (n2[y]) :
        y += 1
        name += (name1 + name2)
        if x<4 :
            continue
        print(name)
