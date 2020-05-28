s1 = "paraparaparadise"
s2 = "paragraph"

# bigramを求める
def gram(seq,num) :
    sen = {seq[n:n+num] for n in range(len(seq) + 1 - num)}
    return sen

X = gram(s1,2)
print(X)
Y = gram(s2,2)
print(Y)

uni = X | Y # Union = 和集合
int_sec = X & Y # Intersection = 積集合
dif = X - Y # difference set = 差集合

print(uni)
print(int_sec)
print(dif)

# in:含まれていたらTrue、含まれていなかったらFalse
print("se" in X) # Xにseが含まれているかどうか
print("se" in Y) # Yにseが含まれているかどうか
