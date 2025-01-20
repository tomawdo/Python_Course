# confrontare ottetto per ottetto l'indirizzo IP con la subnet mask
# stampa finale: gli host sono sulla stessa rete oppure Glo host non sono sulla stessa rete

# 150 & 255 = ?
# 169 & 255 = ?
# 3 & 255 = ?
# 8 & 0 = ?

host_a = "150.169.3.8"
host_b = "150.169.5.2"
sm = "255.255.255.0"

# Split the IP addresses and subnet mask into their components
host_a_parts = list(map(int, host_a.split('.')))
host_b_parts = list(map(int, host_b.split('.')))
sm_parts = list(map(int, sm.split('.')))

# Perform bitwise AND operation for each octet and compare the result
same_network = True
for i in range(4):
    if (host_a_parts[i] & sm_parts[i]) != (host_b_parts[i] & sm_parts[i]):
        same_network = False
        break

if same_network:
    print("Gli host sono sulla stessa rete")
else:
    print("Gli host non sono sulla stessa rete")