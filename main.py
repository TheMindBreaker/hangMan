import os
clear = lambda: os.system('clear')
msg = ''
chose = False
while(chose==False):
    clear()
    print("""

    T)    h)                  M)mm mmm  ##              d) B)bbbb                           k)                           X)    xx Y)    yy Z)zzzzzz
    T)    h)                 M)  mm  mm                 d) B)   bb                          k)                            X)  xx   Y)  yy        Z)
    T)    h)HHHH  e)EEEEE    M)  mm  mm i) n)NNNN   d)DDDD B)bbbb    r)RRR  e)EEEEE a)AAAA  k)  KK e)EEEEE  r)RRR          X)xx     Y)yy       Z)
    T)    h)   HH e)EEEE     M)  mm  mm i) n)   NN d)   DD B)   bb  r)   RR e)EEEE   a)AAA  k)KK   e)EEEE  r)   RR         X)xx      Y)       Z)
    T)    h)   HH e)         M)      mm i) n)   NN d)   DD B)    bb r)      e)      a)   A  k) KK  e)      r)         **  X)  xx     Y)     Z)
    T)    h)   HH  e)EEEE    M)      mm i) n)   NN  d)DDDD B)bbbbb  r)       e)EEEE  a)AAAA k)  KK  e)EEEE r)         ## X)    xx    Y)    Z)zzzzzz
    ===================================================================================================================================================
    """)
    print ('Mensaje ==> '+msg)
    print ("""
    WELCOME TO THE BREAKER-STATION  V. 2.0
    =======================================
    MENU
        1 ===> Ahorcado
        2 ===> Reglas
        3 ===> Funciones
        4 ===> Salir

    """)
    menu_option = input("Opción: ")
    menu_option = menu_option.upper()

    if (menu_option=='1'):
        import game
        fer = game.start();
        if(fer != False):
            msg = ("Ganaste esta ronda y la palabra era ", fer)
        else:
            msg = ("Perdiste la ronda")
        chose ==True
    elif(menu_option=='2'):
        import rules
        rules.show()
        chose ==True
    elif(menu_option=='3'):
        import functions
        functions.show()
        chose ==True
    elif(menu_option=='4' or menu_option=="Salir" or menu_option=="salir" or menu_option=="SALIR"):
        break
    else:
        msg = "La opción elegida no existe, favor de intentar otra"
