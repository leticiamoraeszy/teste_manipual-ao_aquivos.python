<h1 align="center">📁 Manipulação de Arquivos em Python</h1>

<p align="center">
  Um projeto de estudo para praticar leitura, escrita e verificação de arquivos <code>.txt</code> usando Python puro.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-9146FF?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x">
  <img src="https://img.shields.io/badge/status-conclu%C3%ADdo-9146FF?style=for-the-badge" alt="Status: concluído">
  <img src="https://img.shields.io/badge/licença-MIT-9146FF?style=for-the-badge" alt="Licença MIT">
</p>

---

## 📖 Sobre o projeto

Este projeto foi criado para estudar, na prática, como o Python lida com arquivos: como verificar se um arquivo existe, como criá-lo, como escrever e ler seu conteúdo, e como lidar com um problema bem comum no Windows — **erros de codificação (encoding)** ao trabalhar com acentos.

## ⚙️ Funcionalidades

- ✅ Verificar se um arquivo `.txt` existe no diretório
- ✅ Criar um novo arquivo `.txt` caso ele não exista
- ✅ Escrever conteúdo em um arquivo
- ✅ Ler e exibir o conteúdo de um arquivo
- ✅ Leitura correta de acentos e caracteres especiais (UTF-8)

## 🧠 O que eu aprendi

- Como o Python resolve caminhos de arquivo a partir do **diretório de trabalho**, e a diferença entre caminho relativo e absoluto
- Tratamento de exceções com `try / except / else` (e a diferença entre `FileNotFoundError` e `FileExistsError`)
- Uso do gerenciador de contexto `with open(...)`, que fecha o arquivo automaticamente
- Por que arquivos salvos em UTF-8 podem aparecer com caracteres estranhos (`Ã©`, `Ã¡`) no Windows, e como resolver especificando `encoding='utf-8'`

## 📂 Estrutura simplicada do projeto

```
verificação/
└── verificacao/
    ├── arquivo_v.py
    └── arquivo_conteudo
```


## 🚀 Próximos passos

- [ ] Adicionar tratamento para outros formatos de arquivo (`.csv`, `.json`)
- [ ] Criar função de edição/atualização de conteúdo
- [ ] Transformar em um mini CRUD de contatos em arquivo texto

---

<p align="center">
  Feito por <a href="https://github.com/leticiamoraeszy">Letícia Morais</a> 💜
</p>
