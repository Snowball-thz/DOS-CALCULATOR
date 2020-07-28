def main():
    import os
    os.system('clear')
        
    def theme():
        aaa = ('')
        print('''          ***Escolha o tema de sua preferencia***
        01 - Homer Theme
        02 - Cherry Theme ''')
            
        select_theme = input('\n  \033[1mEscolha>>: ')
            
        if select_theme == '1':
            os.system('clear')
            import primary
            primary.alpha()

        elif select_theme == '01':
            os.system('clear')
            primary.alpha()

        elif select_theme == '2':
            os.system('clear')
            import secondary
            secondary.alpha()
                     
        elif select_theme == '02':
            os.system('clear')
            import secondary
            secondary.alpha()

        else:
            print('\033[1;31;47mDigite um argumento válido (Ex: 1; 2)\033[m')
            
    theme()
main()

