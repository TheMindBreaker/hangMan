def start():
    import readwords
    import os
    import mono
    clear = lambda:os.system('clear')
    clear()
    lives = 0
    w_incorrect = []
    w_used = []
    w_correct = []
    secret_word = 'Franc'
    space_word = list('_'*len(secret_word))
    secret_word = secret_word.upper()
    list_sercret_word = list(secret_word)
    msg = ""

    while True:
        if(space_word == list_sercret_word):
            break
            return secret_word
        clear()
        print (lives)
        print (mono.mono[lives])
        print (secret_word)
        print (space_word)
        print (w_used)
        print (w_incorrect)
        print (w_correct)
        print (msg)
        msg = ""
        print (secret_word)
        letter = input("Ingresa un intento: ")
        letter = letter.upper()
        if(len(letter)!=0):
            #Verificacion de longitud
            if(letter in 'ABCDEFGHKIJQLMNÑIOPRSTVWXYZ'):
                #Verificacion de letra valida
                if(letter in w_used):
                    #Verificacion de que no se haya usada
                    msg ="Ya utilizo con anterioridad esta letra"
                else:
                    if(letter in secret_word):
                        #Verificar que la letra este en el arreglo de la palabra
                        if(letter == secret_word):
                            #Verificar si la palabra esta completa y correcta
                            break
                            return secret_word
                        else:
                            for i,k in enumerate(space_word):
                                if(letter == list_sercret_word[i]):
                                    space_word[i] = letter
                                    w_used.append(letter)
                    else:
                        if (lives==5):
                            break
                            return False
                        else:
                            lives = lives + 1
                            w_used.append(letter)
                            w_incorrect.append(letter)
                            msg =("Error la letra ",letter," no esta en la palabra")
            else:
                msg =("Favor de solo ingresar Letras")
        else:
            msg =("Favor de ingresar por lo menos 1 letra :D")
