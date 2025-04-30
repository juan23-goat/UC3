def jogo_da_forca():
    import random
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
    palavra_secreta = random.choice(palavras)
    letras_corretas = set()
    tentativas = 7 
    erros = 0

    forca = [
        """\n
         _______
        |/      
        |      
        |      
        |       
        |      
        |___
        """,
        """\n
         _______
        |/      |
        |      
        |      
        |       
        |      
        |___
        """,
        """\n
         _______
        |/      |
        |      (_)
        |      
        |       
        |      
        |___
        """,
        """\n
         _______
        |/      |
        |      (_)
        |       |
        |       |
        |      
        |___
        """,
        """\n
         _______
        |/      |
        |      (_)
        |      \|
        |       |
        |      
        |___
        """,
        """\n
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      
        |___
        """,
        """\n
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / 
        |___
        """,
        """\n
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / \\
        |___
        """
    ]

    while tentativas > 0:
        palavra_exibida = ""
        for letra in palavra_secreta:
            if letra in letras_corretas:
                palavra_exibida += letra
            else:
                palavra_exibida += "_"
        print(palavra_exibida)

        if palavra_exibida == palavra_secreta:
            print("Parabéns! Você venceu!")
            return

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra.")
        elif letra in palavra_secreta:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            erros += 1
            print("Letra incorreta!")
            print(forca[erros])

        print(f"Tentativas restantes: {tentativas}\n")

    print(f"Game over! A palavra era: {palavra_secreta}")
