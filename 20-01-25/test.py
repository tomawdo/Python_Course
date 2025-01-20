# confrontare ottetto per ottetto l'indirizzo IP con la subnet mask
# stampa finale: gli host sono sulla stessa rete oppure Glo host non sono sulla stessa rete

# 150 & 255 =
# 169 & 255 =
# 3 & 255 =
# 8 & 0 =


host_a = "150.169.3.8"
host_b = "150.169.2.5"
sm = "255.255.255.0"

parti_host_a = list(map(int, host_a.split('.')))
parti_host_b = list(map(int, host_b.split('.')))
parti_sm = list(map(int, sm.split('.')))

intranet = True
for i in range(4):
    if (parti_host_a[i] & parti_sm[i]) != (parti_host_b[i] & parti_sm[i]):
        intranet = False
        break

if intranet:
    print("Gli host sono sulla stessa rete")
else:
    print("Gli host non sono sulla stessa rete")

