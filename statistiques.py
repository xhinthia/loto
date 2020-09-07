
import os
import os.path
import sys
from collections import OrderedDict

chiffretotal=0
chiffre1=0
chiffre2=0
chiffre3=0
chiffre4=0
chiffre5=0
chiffre6=0
chiffre7=0
chiffre8=0
chiffre9=0
chiffre10=0
chiffre11=0
chiffre12=0
chiffre13=0
chiffre14=0
chiffre15=0
chiffre16=0
chiffre17=0
chiffre18=0
chiffre19=0
chiffre20=0
chiffre21=0
chiffre22=0
chiffre23=0
chiffre24=0
chiffre25=0
chiffre26=0
chiffre27=0
chiffre28=0
chiffre29=0
chiffre30=0
chiffre31=0
chiffre32=0
chiffre33=0
chiffre34=0
chiffre35=0
chiffre36=0
chiffre37=0
chiffre38=0
chiffre39=0
chiffre40=0
chiffre41=0
chiffre42=0
chiffre43=0
chiffre44=0
chiffre45=0
chiffre46=0
chiffre47=0
chiffre48=0
chiffre49=0
bonustotal=0
bonus1=0
bonus2=0
bonus3=0
bonus4=0
bonus5=0
bonus6=0
bonus7=0
bonus8=0
bonus9=0
bonus10=0
with open("init.txt","r") as f_read:
	for line in f_read:
		line=line.strip()
		init=int(line)
	f_read.close()
for i in range(1,init):
	with open(str("tirages/"+str(i)),"r") as f_read:
		compteur=0
		for line in f_read:
			compteur+=1
			line=line.strip()
			if str(line)=="1" and compteur<6:
				chiffre1=chiffre1+i
			elif str(line)=="2" and compteur<6:
				chiffre2=chiffre2+i
			elif str(line)=="3" and compteur<6:
				chiffre3=chiffre3+i
			elif str(line)=="4" and compteur<6:
				chiffre4=chiffre4+i
			elif str(line)=="5" and compteur<6:
				chiffre5=chiffre5+i
			elif str(line)=="6" and compteur<6:
				chiffre6=chiffre6+i
			elif str(line)=="7" and compteur<6:
				chiffre7=chiffre7+i
			elif str(line)=="8" and compteur<6:
				chiffre8=chiffre8+i
			elif str(line)=="9" and compteur<6:
				chiffre9=chiffre9+i
			elif str(line)=="10" and compteur<6:
				chiffre10=chiffre10+i

			elif str(line)=="11" and compteur<6:
				chiffre11=chiffre11+i
			elif str(line)=="12" and compteur<6:
				chiffre12=chiffre12+i
			elif str(line)=="13" and compteur<6:
				chiffre13=chiffre13+i
			elif str(line)=="14" and compteur<6:
				chiffre14=chiffre14+i
			elif str(line)=="15" and compteur<6:
				chiffre15=chiffre15+i
			elif str(line)=="16" and compteur<6:
				chiffre16=chiffre16+i
			elif str(line)=="17" and compteur<6:
				chiffre17=chiffre17+i
			elif str(line)=="18" and compteur<6:
				chiffre18=chiffre18+i
			elif str(line)=="19" and compteur<6:
				chiffre19=chiffre19+i
			elif str(line)=="20" and compteur<6:
				chiffre20=chiffre20+i
			
			elif str(line)=="21" and compteur<6:
				chiffre21=chiffre21+i
			elif str(line)=="22" and compteur<6:
				chiffre22=chiffre22+i
			elif str(line)=="23" and compteur<6:
				chiffre23=chiffre23+i
			elif str(line)=="24" and compteur<6:
				chiffre24=chiffre24+i
			elif str(line)=="25" and compteur<6:
				chiffre25=chiffre25+i
			elif str(line)=="26" and compteur<6:
				chiffre26=chiffre26+i
			elif str(line)=="27" and compteur<6:
				chiffre27=chiffre27+i
			elif str(line)=="28" and compteur<6:
				chiffre28=chiffre28+i
			elif str(line)=="29" and compteur<6:
				chiffre29=chiffre29+i
			elif str(line)=="30" and compteur<6:
				chiffre30=chiffre30+i
			
			elif str(line)=="31" and compteur<6:
				chiffre31=chiffre31+i
			elif str(line)=="32" and compteur<6:
				chiffre32=chiffre32+i
			elif str(line)=="33" and compteur<6:
				chiffre33=chiffre33+i
			elif str(line)=="34" and compteur<6:
				chiffre34=chiffre34+i
			elif str(line)=="35" and compteur<6:
				chiffre35=chiffre35+i
			elif str(line)=="36" and compteur<6:
				chiffre36=chiffre36+i
			elif str(line)=="37" and compteur<6:
				chiffre37=chiffre37+i
			elif str(line)=="38" and compteur<6:
				chiffre38=chiffre38+i
			elif str(line)=="39" and compteur<6:
				chiffre39=chiffre39+i
			elif str(line)=="40" and compteur<6:
				chiffre40=chiffre40+i
			
			elif str(line)=="41" and compteur<6:
				chiffre41=chiffre41+i
			elif str(line)=="42" and compteur<6:
				chiffre42=chiffre42+i
			elif str(line)=="43" and compteur<6:
				chiffre43=chiffre43+i
			elif str(line)=="44" and compteur<6:
				chiffre44=chiffre44+i
			elif str(line)=="45" and compteur<6:
				chiffre45=chiffre45+i
			elif str(line)=="46" and compteur<6:
				chiffre46=chiffre46+i
			elif str(line)=="47" and compteur<6:
				chiffre47=chiffre47+i
			elif str(line)=="48" and compteur<6:
				chiffre48=chiffre48+i
			elif str(line)=="49" and compteur<6:
				chiffre49=chiffre49+i
			else:
				if str(line)=="1" and compteur==6:
					bonus1=bonus1+i
				elif str(line)=="2" and compteur==6:
					bonus2=bonus2+i
				elif str(line)=="3" and compteur==6:
					bonus3=bonus3+i
				elif str(line)=="4" and compteur==6:
					bonus4=bonus4+i
				elif str(line)=="5" and compteur==6:
					bonus5=bonus5+i
				elif str(line)=="6" and compteur==6:
					bonus6=bonus6+i
				elif str(line)=="7" and compteur==6:
					bonus7=bonus7+i
				elif str(line)=="8" and compteur==6:
					bonus8=bonus8+i
				elif str(line)=="9" and compteur==6:
					bonus9=bonus9+i
				elif str(line)=="10" and compteur==6:
					bonus10=bonus10+i
			if compteur==6:
				bonustotal+=i
			else:
				chiffretotal+=i


chiffre1=chiffre1/chiffretotal*100
chiffre2=chiffre2/chiffretotal*100
chiffre3=chiffre3/chiffretotal*100
chiffre4=chiffre4/chiffretotal*100
chiffre5=chiffre5/chiffretotal*100
chiffre6=chiffre6/chiffretotal*100
chiffre7=chiffre7/chiffretotal*100
chiffre8=chiffre8/chiffretotal*100
chiffre9=chiffre9/chiffretotal*100
chiffre10=chiffre10/chiffretotal*100

chiffre11=chiffre11/chiffretotal*100
chiffre12=chiffre12/chiffretotal*100
chiffre13=chiffre13/chiffretotal*100
chiffre14=chiffre14/chiffretotal*100
chiffre15=chiffre15/chiffretotal*100
chiffre16=chiffre16/chiffretotal*100
chiffre17=chiffre17/chiffretotal*100
chiffre18=chiffre18/chiffretotal*100
chiffre19=chiffre19/chiffretotal*100
chiffre20=chiffre20/chiffretotal*100

chiffre21=chiffre21/chiffretotal*100
chiffre22=chiffre22/chiffretotal*100
chiffre23=chiffre23/chiffretotal*100
chiffre24=chiffre24/chiffretotal*100
chiffre25=chiffre25/chiffretotal*100
chiffre26=chiffre26/chiffretotal*100
chiffre27=chiffre27/chiffretotal*100
chiffre28=chiffre28/chiffretotal*100
chiffre29=chiffre29/chiffretotal*100
chiffre30=chiffre30/chiffretotal*100

chiffre31=chiffre31/chiffretotal*100
chiffre32=chiffre32/chiffretotal*100
chiffre33=chiffre33/chiffretotal*100
chiffre34=chiffre34/chiffretotal*100
chiffre35=chiffre35/chiffretotal*100
chiffre36=chiffre36/chiffretotal*100
chiffre37=chiffre37/chiffretotal*100
chiffre38=chiffre38/chiffretotal*100
chiffre39=chiffre39/chiffretotal*100
chiffre40=chiffre40/chiffretotal*100

chiffre41=chiffre41/chiffretotal*100
chiffre42=chiffre42/chiffretotal*100
chiffre43=chiffre43/chiffretotal*100
chiffre44=chiffre44/chiffretotal*100
chiffre45=chiffre45/chiffretotal*100
chiffre46=chiffre46/chiffretotal*100
chiffre47=chiffre47/chiffretotal*100
chiffre48=chiffre48/chiffretotal*100
chiffre49=chiffre49/chiffretotal*100

bonus1=bonus1/bonustotal*100
bonus2=bonus2/bonustotal*100
bonus3=bonus3/bonustotal*100
bonus4=bonus4/bonustotal*100
bonus5=bonus5/bonustotal*100
bonus6=bonus6/bonustotal*100
bonus7=bonus7/bonustotal*100
bonus8=bonus8/bonustotal*100
bonus9=bonus9/bonustotal*100
bonus10=bonus10/bonustotal*100

print ("1 : "+str(chiffre1)+"%")
print ("2 : "+str(chiffre2)+"%")
print ("3 : "+str(chiffre3)+"%")
print ("4 : "+str(chiffre4)+"%")
print ("5 : "+str(chiffre5)+"%")
print ("6 : "+str(chiffre6)+"%")
print ("7 : "+str(chiffre7)+"%")
print ("8 : "+str(chiffre8)+"%")
print ("9 : "+str(chiffre9)+"%")
print ("10 : "+str(chiffre10)+"%")

print ("11 : "+str(chiffre11)+"%")
print ("12 : "+str(chiffre12)+"%")
print ("13 : "+str(chiffre13)+"%")
print ("14 : "+str(chiffre14)+"%")
print ("15 : "+str(chiffre15)+"%")
print ("16 : "+str(chiffre16)+"%")
print ("17 : "+str(chiffre17)+"%")
print ("18 : "+str(chiffre18)+"%")
print ("19 : "+str(chiffre19)+"%")
print ("20 : "+str(chiffre20)+"%")

print ("21 : "+str(chiffre21)+"%")
print ("22 : "+str(chiffre22)+"%")
print ("23 : "+str(chiffre23)+"%")
print ("24 : "+str(chiffre24)+"%")
print ("25 : "+str(chiffre25)+"%")
print ("26 : "+str(chiffre26)+"%")
print ("27 : "+str(chiffre27)+"%")
print ("28 : "+str(chiffre28)+"%")
print ("29 : "+str(chiffre29)+"%")
print ("30 : "+str(chiffre30)+"%")

print ("31 : "+str(chiffre31)+"%")
print ("32 : "+str(chiffre32)+"%")
print ("33 : "+str(chiffre33)+"%")
print ("34 : "+str(chiffre34)+"%")
print ("35 : "+str(chiffre35)+"%")
print ("36 : "+str(chiffre36)+"%")
print ("37 : "+str(chiffre37)+"%")
print ("38 : "+str(chiffre38)+"%")
print ("39 : "+str(chiffre39)+"%")
print ("40 : "+str(chiffre40)+"%")

print ("41 : "+str(chiffre41)+"%")
print ("42 : "+str(chiffre42)+"%")
print ("43 : "+str(chiffre43)+"%")
print ("44 : "+str(chiffre44)+"%")
print ("45 : "+str(chiffre45)+"%")
print ("46 : "+str(chiffre46)+"%")
print ("47 : "+str(chiffre47)+"%")
print ("48 : "+str(chiffre48)+"%")
print ("49 : "+str(chiffre49)+"%")
print ("")
print ("Bonus 1 : "+str(bonus1)+"%")
print ("Bonus 2 : "+str(bonus2)+"%")
print ("Bonus 3 : "+str(bonus3)+"%")
print ("Bonus 4 : "+str(bonus4)+"%")
print ("Bonus 5 : "+str(bonus5)+"%")
print ("Bonus 6 : "+str(bonus6)+"%")
print ("Bonus 7 : "+str(bonus7)+"%")
print ("Bonus 8 : "+str(bonus8)+"%")
print ("Bonus 9 : "+str(bonus9)+"%")
print ("Bonus 10 : "+str(bonus10)+"%")
continuer=input()