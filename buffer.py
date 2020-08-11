a=1
while a==1:
	with open("init.txt","r") as f_read:
		for line in f_read:
			line=line.strip()
			init=line
	f_read.close()
	print ("Souhaitez-vous ajouter un nouveau tirage à l'historique ?")
	print ("")
	print ("1 - Oui")
	print ("2 - Non (cette action quitte la fenêtre)")
	b=1
	while b==1:
		choix=input()
		if str(choix)=="1":
			numero_manquant=5
			bonus_manquant=1
			print ("NOUVEAUX TIRAGE")
			#chiffre déjà entrés
			print ("1 - Valider (Vous devez ajouter "+str(numero_manquant)+" et "+str(bonus_manquant)+" pour valider ce nouveau tirage)")
			print ("2 - Réinitialiser les numéros")
			print ("3 - Ajouter un nouveau numéro")
			print ("0 - Quitter (cette action quitte la fenêtre)")
		elif str(choix)=="2":
			quit()
		else:
			pass
