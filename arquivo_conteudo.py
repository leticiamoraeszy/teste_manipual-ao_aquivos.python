def mostrarconteudo(nome):
    with open(nome, 'rt', encoding='utf-8') as arquivo:   # chamada para abrir aquivo
        conteudo = arquivo.read() # lendo o arquivo para ver o conteúdo
        print(conteudo) #printando conteúdo para verificar oque tem dentro dele