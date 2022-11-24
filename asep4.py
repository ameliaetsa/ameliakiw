print("="*19, "CAFE", "="*19)
print("="*10, "MASUKKAN JUMLAH PESANAN", "="*9)
c= int(input("CAPPUCINO\t DISKON 50%\t Rp 25.000 : "))
v= int(input("VANILLA LATTE\t DISKON 65%\t Rp 22.000 : "))
a= int(input("AMERICANO\t DISKON 35% \t Rp 20.000 : "))
b= int(input("BREWED COFFEE\t DISKON 40%\t Rp 20.000 : "))
cappucino= 25000*c
dc=50/100*cappucino
vanilla=22000*v
dv=65/100*vanilla
americano=30000*a
da=35/100*americano
brewed=20000*b
db=40/100*brewed
print("="*17, "TOTAL", "="*17)
print(f"TOTAL CAPPUCINO\t : Rp round{dc}")
print("TOTAL VANILLA LATTE\t : Rp round{dv}")
print("TOTAL AMERICANO\t : Rp round{da}")
print("TOTAL BREWED COFFEE\t : Rp round{db}")

