from tkinter import *
import PIL.ImageGrab
from time import time
from PIL import ImageGrab


hauteur=800
largeur=1300
milieu_y=hauteur//2
milieu_x=largeur//2
iteration=-1
niveauzoom=1


reglec="1450451"
reglec="1040524"
reglec="1044205"
reglec="1505111"
reglec="200"
regle=[int(i) for i in reglec]

def vers(regle=regle):
	global niveauzoom, etapes
	debut=time()
	# global iteration

	# if iteration<0:
	# 	iteration=int(Itera.get())
	# 	Canevas.delete(ALL)

	#Initalisation
	chiffre_regle_en_cours=0
	deplacement=[(4*niveauzoom,0),(2*niveauzoom,3*niveauzoom),(-2*niveauzoom,3*niveauzoom),(-4*niveauzoom,0),(-2*niveauzoom,-3*niveauzoom),(2*niveauzoom,-3*niveauzoom)]
	situations_connues={}
	chemins_parcourus=[(milieu_x+deplacement[0][0]/2,milieu_y)]
	direction=0
	direction_precedente=0
	direction_absolue=0
	x=milieu_x+deplacement[0][0]
	y=milieu_y
	etapes=0
	couleurs=["purple","red","cyan","blue","pink","green","orange"]
	dessin(milieu_x,milieu_y,x,y,couleurs[1])



	#verif directions dispos
	while 1:
		etapes+=1
		libre=""
		occupe=""
		for i in range(len(deplacement)):
			if (x+deplacement[i][0]/2,y+deplacement[i][1]/2) in chemins_parcourus:
				occupe+=str((i-direction_absolue)%6)
			else:
				libre+=str((i-direction_absolue)%6)
		temp=[i for i in libre]
		temp.sort()
		libre=''.join(temp)

		#print(libre,occupe)

		#Choix de la nouvelle direction
		if len(libre)==0:
			#plus de chemin dispo
			#print("stop")
			break
		elif len(libre)==1:
			#un seul chemin dispo
			direction=int(libre)
			couleur="black"
		elif libre in situations_connues.keys():
			#on connaît déjà cette situation
			direction=situations_connues[libre][0]
			couleur=situations_connues[libre][1]
			#print("connu")
		else:
			#nouvelle situation, on utilise la règle suivante
			direction=regle[chiffre_regle_en_cours]
			chiffre_regle_en_cours=(chiffre_regle_en_cours + 1)%len(regle)
			couleur=couleurs[chiffre_regle_en_cours]
			situations_connues[libre]=(direction,couleur)
			#print("nouveau")
		
		#on calcule la directiona absolue
		#print(direction_precedente)
		direction_absolue=(direction_absolue+direction)%6
		direction_precedente=direction
		chemins_parcourus.append((x+deplacement[direction_absolue][0]/2,y+deplacement[direction_absolue][1]/2))
		#print(direction_precedente,direction,direction_absolue)

		#Affichage
		x2=x+deplacement[direction_absolue][0]
		y2=y+deplacement[direction_absolue][1]
		dessin(x,y,x2,y2,couleur)
		x=x2
		y=y2
	print(etapes,time()-debut)

	#recursif = fenetre.after(50,vers)

	# if iteration>0:
	# 	iteration-=1
	# 	numero.set(int(Itera.get())-iteration)
	# else:
	# 	fenetre.after_cancel(recursif)
	# 	iteration=-1
	# 	numero.set(0)

	#fenetre.after_cancel(recursif)

def dessin(x,y,x2,y2,couleur):
	Canevas.create_line(x,y,x2,y2,fill=couleur)
	#fenetre.after(100,dessin)

def zoom_worms(niveau_zoom):
	global niveauzoom
	niveauzoom=int(niveau_zoom)
	Canevas.delete(ALL)


def save_vers():
	global etapes
	x = Canvas.winfo_rootx(Canevas)
	y = Canvas.winfo_rooty(Canevas)
	w = Canvas.winfo_width(Canevas)
	h = Canvas.winfo_height(Canevas)
	print(x,y,w,h)
	#img= ImageGrab.grab((x, y, x+w, y+h)).save("IMAGE.png")
	img= ImageGrab.grab((0, 0, 2735, 1600)).save(reglec+" "+str(etapes)+" étapes.png")



fenetre=Tk()

fenetre.attributes('-fullscreen', True)
fenetre.bind('<Escape>',lambda e: fenetre.destroy())

Canevas=Canvas(fenetre,height=hauteur,width=largeur)
Canevas.pack()

Worm = Button(fenetre,  text = 'Lancer le turmite',  command = vers)
Worm.pack()

BoutonSave = Button(fenetre,  text = 'Save',  command = save_vers)
BoutonSave.pack()

# Bouton1 = Button(fenetre,  text = 'Quitter',  command = fenetre.destroy)
# Bouton1.pack()

# Itera=StringVar()
# Itera.set(10)

# numero=StringVar()
# numero.set(0)



zoom=StringVar()
zoom.set(1)
zoom_vers=Scale(fenetre,  orient='horizontal',  from_=1,  to=10,  resolution=1,  \
tickinterval=2,  label='Zoom',  variable=zoom,  command=zoom_worms)
zoom_vers.pack()

fenetre.mainloop()

# rgb = PIL.ImageGrab.grab().load()[milieu,milieu]
# print(rgb)