import os 
while True:
	verif = input('B to quit and other to continue')
	if verif == "B":
		break
	fichier = open('/etc/asterisk/sip.conf','a')
	tel = input('numero de tel : ')
	user = input('user de tel : ')
	mdp = input('mot de passe : ')
	fichier.write('\n['+user+']\n username ='+user+';\n secret = bonjour;\n host=dynamic;\n type=friend;\n context=local;')
	f2 = open('/etc/asterisk/extensions.conf','a')
	f2.write('\nexten =>'+tel+',1,Dial(SIP/'+user+',15)\nexten =>'+tel+',2,Hangup()')
	fichier.close()
	f2.close()
	os.system('sudo asterisk -rvvvvvvvvvv')
	os.system('sip reload')
	os.system('dialplan')
	os.system('reload')
	os.system('exit')
	os.system('sudo systemctl restart asterisk.service')



