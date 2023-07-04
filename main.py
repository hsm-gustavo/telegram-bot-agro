import openai
import telebot
from os import getenv
from requests import get as requests_get
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = getenv("BOTAPI_TOKEN")
openai.api_key = getenv("OPENAI_API_KEY")
openai.organization = getenv("OPENAI_ORG")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['sobre'])
def sobre(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['sobre']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['info'])
def info(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['info']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['docentes'])
def docentes(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['docentes']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['disciplinas'])
def disciplinas(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['disciplinas']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['geral'])
def geral(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['geral']
    bot.send_message(message.chat.id, texto)
    
@bot.message_handler(commands=['matricula', 'certidao', 'ementas', 'historico'])
def sistema(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['sistema']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['assinatura'])
def assinatura(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['assinatura']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['trancar'])
def trancar(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['trancar']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['rematricula'])
def rematricula(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['rematricula']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['dispensa'])
def dispensa(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['dispensa']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['buscar'])
def busca(message):
    bot.send_message(message.chat.id, "Digite sua dúvida:")
    bot.register_next_step_handler(message, busca2)

def busca2(message):
    bot.send_message(message.chat.id, "Aguarde um momento, estamos buscando a resposta...")
    prompt = message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + " Máximo tamanho de resposta: 30 palavras. Se necessário informações adicionais Campus: UFAL ARAPIRACA, Curso: AGRONOMIA",
        temperature=0.2,
        max_tokens=300,
    )
    bot.send_message(message.chat.id, response.choices[0].text)

@bot.message_handler(commands=['horarios'])
def horario(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['horarios']
    bot.send_message(message.chat.id, texto)


@bot.message_handler(commands=['redirecionar'])
def redirecionar(message):
    json = requests_get("https://api.npoint.io/e72dba775c7bf86ed85d").json()
    texto = json['redirecionar']
    bot.send_message(message.chat.id, texto)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = f"""
    Olá, {message.from_user.first_name}!
Escolha uma opção para continuar (clique no item ou digite o comando):

/sobre - Sobre o curso

/info - Onde posso me informar sobre o curso

/docentes - Quem são os docentes do curso

/disciplinas - Onde posso ver as disciplinas do curso

/geral - Dúvidas gerais sobre a UFAL

/horarios - Horários de aula

/buscar - Minha dúvida não está aqui

/redirecionar - Desejo falar com a coordenação do curso

    Clique em uma das opções acima."""
    # placeholder for any message
    bot.send_photo(message.chat.id, photo=open("logo.jpg", "rb"), caption=texto)
    

# creates an infinite loop for the bot to listen to messages
bot.infinity_polling()
