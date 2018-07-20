from main import app
from flask import render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

english_bot = ChatBot("botname", 
                        storage_adapter="chatterbot.storage.SQLStorageAdapter",
                        database_uri="postgres://username:password@localhost:5432/database")

english_bot.set_trainer(ChatterBotCorpusTrainer)
# Uncomment to activate the trainer-file you want to use
english_bot.train("chatterbot.corpus.swedish", "chatterbot.corpus.custom")
#english_bot.train("chatterbot.corpus.english")

@app.route("/")
def chatbot():
    return render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))