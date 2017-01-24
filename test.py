import redis
'''
Cette methode est appelee dans un thread et va afficher en boucle les messages du channel qui arrive
message - le message qui sera affiche 
'''

def my_handler(message):
	print(message)['data']

try:
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	p = r.pubsub()
	p.subscribe(**{'chat': my_handler})
	thread = p.run_in_thread(sleep_time=0.001)

	print('Bienvenue')
	pseudo = raw_input('Choisir un pseudo : ')

	msg = None
	while(msg != 'exit'):
		msg = raw_input()
		if(msg != 'exit'):
			r.publish('chat', pseudo + ' : ' + msg)

	thread.stop()
except redis.exceptions.ConnectionError as e:
	print "Erreur - Le serveur Redis n'a pas ete lance !"




	
