"""pt = 0
q = 1
while q <=3:
    rpt = input(f"Resposta {q}:")
    if q == 1 and rpt == "b":
        pt = pt+1
    elif q == 2 and rpt == "b":
        pt = pt+1
    elif q == 3 and rpt == "b":
        pt = pt+1
    q = q+1

print(f"Você fez {pt} pontos.")"""
"""
n = 1
s = 0
while n <= 10:
    x=float(input(f"digite numero"))
    s+=x
    n += 1
print(f"Soma={s:.2f}")
print(f"media={s/(n-1)}")"""
"""
d=float(input(f"qual deposito?"))
t=float(input(f"qual taxa de juros?"))/100
m=0
n=int(input(f"Quanto você vai colocar por mês?"))
while m <= 24:

    print(f"mês {m}, poupança R${d:.2f}")
    d+=(d*t)+n
    m+=1
"""
s=0
while True:
    n=input("digite")
    if n =="sair":
        break
    n=float(n)
    s+=n
print(s)
