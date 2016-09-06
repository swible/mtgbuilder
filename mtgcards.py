import json

#search =  'the '
#print ('Loading file...')
#json_file = open(filename)
#json_data = json.load(json_file)
#json_file.close()

#print ('File loaded now searching...')
#cards = 0
#for key in json_data.keys() :
#	print(key)
#	cards +=1

#newList = [ word for word in card_names if word.casefold().startswith(search.casefold()) ]
#rint (newList)

#returns a *list* of card names starting or matching with the card_name_search *str*:
#def searchCardName(card_name_search):
#	card_names = json_data.keys()
#	return [ name for name in card_names if name.casefold().startswith(card_name_search.casefold()) ]

#returns a *dict* of card info identified by the card_name *str*
#def getCardInfo(card_name):
#	return json_data.get(card_name)

#calculates the deck size based of deck dictionary
def deckSize(deck):
	count = 0
	for card_quantity in deck.values():
		count += card_quantity
	return count

#loads a .dec file and return a *dict* = key is the card name and value is the quantity
def loadDeck(file_name):
	deck = {}
	deck_file = open(file_name)
	for line in deck_file: #can it be improved?
		if len(line.strip()) > 0:
			line_list = line.rstrip('\n').split(' ', 1)
			deck[line_list[1]] = int(line_list[0])
	return deck 

#add each card to a list from card name and quantity from dict
def buildDeck(deck_dict):
	deck_list = []
	for card_name, quantity in deck_dict.items():
		for _ in range(quantity):
			deck_list.append(card_name)
	return deck_list
	
	


	
#the_deck_dict = loadDeck('vampire-maggro.dec')
#the_deck_list = buildDeck(the_deck_dict)
#for card in the_deck_list:
#	print (getCardInfo(card).get('cmc'))
#print (searchCardName('swam'))
#print (getCardInfo('Combo Player'))

#Class for MTG Json data file
class mtgJson:
	def __init__(self, json_filename):
		json_file = open(json_filename)
		self.json_data = json.load(json_file) #error checking
		json_file.close()
	
	#returns a *list* of card names starting or matching with the card_name_search *str*:
	def searchCardName(self, card_name_search):
		card_names = self.json_data.keys()
		return [ name for name in card_names if name.casefold().startswith(card_name_search.casefold()) ]
	
	#returns a *dict* of card info identified by the card_name *str*
	def getCardInfo(self, card_name):
		return self.json_data.get(card_name)

	def getCardList(self):
		return list(self.json_data.keys())

#filename = 'AllCards.json'
#card_db = mtgJson(filename)
#card_name = input('What card do you want to look for?')
#print (card_name)
#for card in card_db.searchCardName(card_name):
#	print (card)

#test = mtgJson()
		
#test commit
	
	