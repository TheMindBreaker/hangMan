
def show():
    import os
    clear = lambda: os.system('clear')
    msg = ''
    while True:
        clear()
        import os

        print("""

        T)    h)                  M)mm mmm  ##              d) B)bbbb                           k)                           X)    xx Y)    yy Z)zzzzzz
        T)    h)                 M)  mm  mm                 d) B)   bb                          k)                            X)  xx   Y)  yy        Z)
        T)    h)HHHH  e)EEEEE    M)  mm  mm i) n)NNNN   d)DDDD B)bbbb    r)RRR  e)EEEEE a)AAAA  k)  KK e)EEEEE  r)RRR          X)xx     Y)yy       Z)
        T)    h)   HH e)EEEE     M)  mm  mm i) n)   NN d)   DD B)   bb  r)   RR e)EEEE   a)AAA  k)KK   e)EEEE  r)   RR         X)xx      Y)       Z)
        T)    h)   HH e)         M)      mm i) n)   NN d)   DD B)    bb r)      e)      a)   A  k) KK  e)      r)         **  X)  xx     Y)     Z)
        T)    h)   HH  e)EEEE    M)      mm i) n)   NN  d)DDDD B)bbbbb  r)       e)EEEE  a)AAAA k)  KK  e)EEEE r)         ## X)    xx    Y)    Z)zzzzzz
        ===================================================================================================================================================
        """)
        print ('Mensages ==>'+msg)
        print ("""
        WELCOME TO THE BREAKER-STATION  V. 2.0
        =======================================
        FUNCTIONS
            1 ===> Agregar palabra
            4 ===> Regresar

        """)
        menu_option = input("Selecciona una opción: ")
        menu_option = menu_option.upper()
        if(menu_option=='1'):
            while True:
                try:
                    palabra = str(input("Ingresa una palabra: "))
                except ValueError:
                    msg = "Error esta no es una palabra."
                    continue
                else:
                    break
            add = open('words.txt','a+')
            add.write(palabra + "\n")
            msg = 'Palabra ' + palabra +' fue agregada con exito'
        elif(menu_option=='4'):
            break
        else:
            msg = 'La opcion '+menu_option+' elegida no es valida'
