def alpha():
    try:
        import os
        os.system('clear')
    
        def start():
            import theme01
            theme01.theme()

            escolha = int and float(input('\n\n     Operador>>: '))

            #Adição
            if escolha == 1:
                aaa = int and float(input('\nDigite o primeiro número: '))
                aab = int and float(input('Digite o segundo número: '))
                print('\n O resultado da soma é {}.' .format(aaa + aab))
                retun = input('\n\033[1mPressione ENTER para prosseguir...')
                os.system('clear')
                start()

            #Subtração
            elif escolha == 2:
                aaa = int and float(input('\nDigite o primeiro número: '))
                aab = int and float(input('Digite o segundo número: '))
                print('\n O resultado da subtração é {}.' .format(aaa - aab))
                retun = input('\n\033[1mPressione ENTER para prosseguir...')
                os.system('clear')
                start()

            #Multiplicação
            elif escolha == 3:
                aaa = int and float(input('\nDigite o primeiro número: '))
                aab = int and float(input('Digite o segundo número: '))
                print('\n O resultado da multiplicação é {}.' .format(aaa * aab))
                retun = input('\n\033[1mPressione ENTER para prosseguir...')
                os.system('clear')
                start()

            #Divisão
            elif escolha == 4:
                try:
                    aaa = int and float(input('\nDigite o primeiro número: '))
                    aab = int and float(input('Digite o segundo número: '))
                    print('\n O resultado da divisão é {}.' .format(aaa / aab))
                    retun = input('\n\033[1mPressione ENTER para prosseguir...')
                    os.system('clear')
                    start()
                except ZeroDivisionError:
                    print('\n O resultado da divisão é {}.' .format(0))
                    retun = input('\n\033[1mPressione ENTER para prosseguir...')
                    os.system('clear')
                    start()

            #Potencia
            elif escolha == 5:
                aaa = int and float(input('\nDigite o primeiro número: '))
                aab = int and float(input('Digite o segundo número: '))
                print('\n O resultado da potencia é {}.' .format(aaa ** aab))
                retun = input('\n\033[1mPressione ENTER para prosseguir...')
                os.system('clear')
                start()

            #Porcentagem
            elif escolha == 6:
                aaa = int and float(input('\nDigite o primeiro número: '))
                aab = int and float(input('Digite o segundo número: '))
                print('\n O resultado da porcentagem é {}.' .format(aaa % aab))
                retun = input('\n\033[1mPressione ENTER para prosseguir...')
                os.system('clear')
                start()

            else:
                os.system('clear')
                print('\033[1;31;47mDigite um argumento válido.\033[m')
                start()

        start()
    except KeyboardInterrupt:
        import os
        import time
        os.system('clear')
        print('\033[1m Fechando Programa. Volte Sempre \033[m')
        time.sleep(0.7)
        print('\n\033[1msave DataFile...\033[m')
        time.sleep(0.3)
        print('\033[1msave SecurityData...\033[m')
        time.sleep(0.3)
        print('\033[1msave BackupData...\033[m')
        time.sleep(0.3)
        print('\033[1mAnalizing residual cache...\033[m')
        time.sleep(0.3)
        print('\033[1mDelete last cache...\033[m')
        time.sleep(0.3)
        print('\033[1mDelete last data...\033[m')
        time.sleep(0.3)
        exit
    
    except ValueError:
        import os
        os.system('clear')
        print('Erro de valores')
        alpha()
