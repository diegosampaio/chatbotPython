from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Charlie")

conversa = [
    'Oi', 'Olá', 'Como vai você?', 'Estou Ótimo!', 'Que bom!', 'Obrigado', 'De nada', 'O que você gosta de fazer?', 'aprender', 'a programar'
]

treino = ListTrainer(bot)
treino.train(conversa)

print('Oi, meu nome é Charlie, sou um chatbot e estou aprendendo a conversar, vamos conversar?')

while True:
    try:
        pergunta = input("Você: ")
        resposta = bot.get_response(pergunta)        
        print('Charlie: ', resposta)


    except(KeyboardInterrupt, EOFError, SystemExit):
        break