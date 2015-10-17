#print("pozdravjeni vsi")
#print ("hrcek")

name1 = "neja"
name2 = "valentina"
name = "MOMO"
#print("zdravo nekdo")
#if name == name1:
#	print("oo neja")
# elif name == name2:
# 	print("brrrr")
# else:
# 	print("mjav")
	


def dober_dan(name):
	print("heja ho " + name)

def lepo_pozdravi(name):
	clani = ["valentina", "neja", "miha"]
	if name in clani:
		dober_dan(name)
	else:
		print("malo sem se zmedla")
uletavci = ["kaja", "boris", "sasa", "hruska", "miha", "srna"]

for u in uletavci:
	dober_dan(u)

lepo_pozdravi("kaja")
lepo_pozdravi("boris")
lepo_pozdravi("sasa")
lepo_pozdravi("miha")

dober_dan(uletavci[0])



# dober_dan("hrcek")
# dober_dan("django")
# dober_dan(name)
# clani = ["valentina", "neja", "miha"]
# if name in clani:
# 	dober_dan(name)
# else:
# 	print("tebe pa se ne poznam")
