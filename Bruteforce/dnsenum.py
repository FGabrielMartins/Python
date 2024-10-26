import dns.resolver

res = dns.resolver.Resolver()

alvo = "bancocn.com"

try:
    resultado = res.resolve(alvo, "A")
    for ip in resultado:
        print(alvo,"->", ip)  
except:
    pass