with open("init.txt","r") as f_read:
	for line in f_read:
		line=line.strip()
		init=line
f_read.close()
print ("Souhaitez-vous ajouter un nouveau tirage à l'historique ?")
print ("")
print ("1 - Oui")
print ("2 - Non (cette action quitte la fenêtre)")
a=1
while a==1:
	choix_a=input()
	if str(choix_a)=="1":
		b=1
		while b==1:
			numero1=0
			numero2=0
			numero3=0
			numero4=0
			numero5=0
			bonus1=0
			numero_manquant=5
			bonus_manquant=1
			c=1
			while c==1:
				print ("**********************************")
				print ("")
				print ("		NOUVEAU TIRAGE")
        		print ("")
        		print ("**********************************")
        		print ("")
        		print ("<><><><><><><><><><><><><><><><><>")
        		print ("")
        		if str(numero1)!=0:
        			print ("1e numéro : "+str(numero1))
        		if str(numero2)!=0:
        			print ("2e numéro : "+str(numero2))
        		if str(numero3)!=0:
        			print ("3e numéro : "+str(numero3))
        		if str(numero4)!=0:
        			print ("4e numéro : "+str(numero4))
        		if str(numero5)!=0:
        			print ("5e numéro : "+str(numero5))
				print ("")
				if str(bonus1)!=0:
					print ("Numéro bonus : "+str(bonus1))
				print ("")
				print ("<><><><><><><><><><><><><><><><><>")
				print ("")
				print ("")
				print ("1 - Valider (Vous devez ajouter "+str(numero_manquant)+" et "+str(bonus_manquant)+" pour valider ce nouveau tirage)")
				print ("2 - Réinitialiser les numéros")
				print ("3 - Ajouter un nouveau numéro")
				print ("0 - Quitter (cette action quitte la fenêtre)")
				choix_c=input()
				if str(choix_c)=="0":
					quit()
				elif str(choix_c)=="1":
					if numero_manquant==0 and bonus_manquant==0:
						fw = open(str("tirages/"+str(init)),"w")
						fw.write(str(numero1))
						fw.write("\n")
						fw.write(str(numero2))
						fw.write("\n")
						fw.write(str(numero3))
						fw.write("\n")
						fw.write(str(numero4))
						fw.write("\n")
						fw.write(str(numero5))
						fw.write("\n")
						fw.write(str(bonus1))
						fw.close()
						init+=1
						if os.path.isfile("init.txt")=="true":
							os.remove("init.txt")
						fw = open("init.txt","w")
						fw.write(str(init))
						fw.close()
						print ("Nouveau tirage ajouté !")
						print ("")
						terminer=input("Appuyez sur une touche pour fermer...")
					else:
						print ("Vous devez entrer les 5 numéros et le numéro bonus !")
						pass
				elif str(choix_c)=="2":
					c=0
					pass
				elif str(choix_c)=="3":
					if numero_manquant>0:
						d=1
						while d==1:
							choix_d=input("Veuillez entrer un chiffre entre 1 et 49 : ")
							try:
								choix_d=int(choix_d)
							except:
								pass
							if choix_d in range (1,50):
								if numero1==0:
									numero1=choix_d
								elif numero2==0:
									numero2=choix_d
								elif numero3==0:
									numero3=choix_d
								elif numero4==0:
									numero4=choix_d
								elif numero5==0:
									numero5=choix_d
								d=0
								numero_manquant-=1
							else:
								pass
					elif numero_manquant==0 and bonus_manquant==1:
						d=1
						while d==1:
							choix_d=input("Veuillez entrer un chiffre entre 1 et 10 : ")
							try:
								choix_d=int(choix_d)
							except:
								pass
							if choix_d in range (1,11):
								bonus1=choix_d
								d=0
								bonus_manquant-=1
							else:
								pass
					else:
						print ("Vous avez déjà entré les 5 numéros et le bonus, vous devez soit valider soit réinitialiser !")
						pass
	elif str(choix_a)=="2":
		quit()
	else:
		pass
