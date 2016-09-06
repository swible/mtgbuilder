from flask import Flask, redirect, url_for, jsonify, render_template
from mtgcards import mtgJson

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cardinfo/<string:cardname>', methods=['GET'])
def get_cardinfo(cardname):
	card_db = mtgJson('AllCards.json')
	card = card_db.getCardInfo(cardname)
	return jsonify(card)

@app.route('/cardsearch/<string:cardname>', methods=['GET'])
def get_cardsearch(cardname):
	card_db = mtgJson('AllCards.json')
	search_result = card_db.searchCardName(cardname)
	return jsonify(search_result)

@app.route('/cardlist', methods=['GET'])
def get_cardlist():
	card_db = mtgJson('AllCards.json')
	card_list = card_db.getCardList()
	return jsonify(card_list)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

#test
