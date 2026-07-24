from verificação.arquivo_v import verificarExiste
from verificação.arquivo_conteudo import mostrarconteudo

aqr = 'letyjourney.txt'

if verificarExiste(aqr):
    print('Aquivo  encontrado')
else:
    print('Aquivo não encontrado')

mostrarconteudo('letyjourney.txt')