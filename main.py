
import random
import re


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?¿!-_]\s*',user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message,recognized_words,single_response=False,required_word=[] ):
    #en la definición anterior se pasan los datos para calcular qué mensaje mostrará
    message_certanly = 0
    has_requiered_words = True
    #Se procede a iterar las palabras del mensaje
    for word in user_message:
        #Se procede a detectar palabras reconocidas
        if word in recognized_words:
            message_certanly +=1
            #Aumenta la probabilidad de encontrar una
    percentage = float(message_certanly)/float(len(recognized_words) ) #Aquí se calcula el porcentaje de certeza de qué mensaje contestará en base a palabras clave
    for word in required_word:
        #Valida existencia de palabras requeridas en el mensaje
        if word not in user_message:
            has_requiered_words = False
            break
    if has_requiered_words or single_response:
        return int(percentage * 100) #Devuelve el porcentaje multiplicado X 100 de cada respuesta
    else:
        return 0
def check_all_messages(message):
        highest_prob = {}
        def response(bot_response,list_of_words,single_response = False,required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message,list_of_words, single_response,required_words)
        #casos de respuesta
        response('Hola',['hola','ola','hi','buenas','saludos'],single_response = True)
        response('Estoy bien y tu?',['como','estas','va','vas','sientes'],required_words=['como'])
        response('Genial!, en qué te puedo ayudar?',['bien','excelente'],single_response = True)
        response('Oh no!, en qué te puedo ayudar?',['mal','horrible','terrible'],single_response = True)
        response('Estamos ubicados en Managua, Nicaragua',['ubicados','direccion','ubicado','lugar'],single_response=True)
        response('Puedes contactarnos en el apartado de contacto de la página!',['correo','numero','gerente','empleado','personalizado','contacto','contactarlos',
        'contactanos'],single_response = True)
        response('Un placer estar a su servicio!',['gracias','te lo agradezco','thanks','adios'],single_response = True)
        response('Puedes encontrar shorts en el apartado de productos y utilizando el filtro o con el buscador! :)',
        ['shorts','pantalonsillos','corto','bermudas'],single_response = True)
        response('Puedes encontrar gorras en el apartado de productos y utilizando el filtro o con el buscador! :)',
        ['gorras','gorra','sombrero','cabeza','accesorio','accesorios'],single_response = True)
        response('Puedes encontrar camisas en el apartado de productos y utilizando el filtro o con el buscador! :)',
        ['camisas','camisa','camiseta','camisetas','polo','polos','manga larga','manga'],single_response = True)
        
        best_match = max(highest_prob, key=highest_prob.get)
        #Hprint(highest_prob)
        return unknown() if highest_prob[best_match] < 1 else best_match
def unknown():
    response = ['Puedes decirlo de nuevo?','No estoy seguro de lo que quieres :(','No conozco la respuesta :('][random.randrange(3)]
    return response
    
while True:
    
    print("Bot : "+ get_response(input('You :')))