meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Respuesta a una broma",
            "SHEESH": "Expresió de ligera desaprobación",
            "CREEPY": "Algo aterrador",
            "AGGRO": "Que una persona se enfade agresivamente",
            }
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        if word == "Diccionario":
            print(meme_dict)
        else:
            print("No se ha encontrado esta palabra.")



