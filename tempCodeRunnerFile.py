while True:
    print("=== MENU ===")
    print("(1) Quit"), print ("(2) Enter")
    Confirmacao = int(input(": ").strip()) 
    if Confirmacao == 1:
        print("quebrou")
        break
    elif Confirmacao == 2:
        print("=== Cadastro ===")
        cadastro = input("Nome :")
        cadastro = input ("Senha :")
        print("=== Cadastro concluído ===")
        print("(1) Fazer outro login"), print("(2) Finalizar")
        Confirmacao2 = int(input(": ").strip())
        if Confirmacao2 == 1:
            continue 
        elif Confirmacao2 == 2:
            print("Agradecemos seu cadastro") 
            break
        else:
            print("responda com 1 ou 2")
    
    else:
        print("responda com 1 ou 2" )

