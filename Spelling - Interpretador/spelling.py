#Importação das bibliotecas usadas no código
import random
from tkinter import *
from tkinter import messagebox
import pygame

#Função de ordenação Bolha
def bolha(lista):
    trocou = True
    fim = len(lista) - 1
    while fim > 0 and trocou:
        trocou = False
        for i in range(0, fim):
            if lista[i] < lista[i + 1]:
                trocou = True
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
        fim = fim - 1

#Lista com o alfabeto para puxar as letras no jogo
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sequenciaJogo = []
pontos = 0

#Lista onde ficarão os nomes em ranking dos jogadores
ranking = []

#Abrindo o arquivo txt do ranking para puxar os nomes já existentes nele e salvar na respectiva lista
rankingArquivo = open('ranking.txt', 'r')
for linha in rankingArquivo.readlines():
    if linha[0] in '0123456789':
        ranking += [linha]
rankingArquivo.close()


#Definindo a Janela e algumas propriedades
janela = Tk()
janela.title('Spelling')
janela.geometry('1400x777+-10+0')
janela.iconbitmap(default='telas/iconespelling.ico')
janela.resizable(width=0, height=0) #Deixando o tamanho da tela fixo


#Função para resetar a janela toda vez que for trocar de tela
def resetaJanela():
    imgPadrao = PhotoImage(file='telas/telainicial.png') #Poderia ser qualquer imagem
    labPadrao = Label(janela, image=imgPadrao)
    labPadrao.place(x=-1, y=-1)


#Função da tela inicial do jogo (menu)
def telaInicial():
    global sequenciaJogo
    global pontos
    sequenciaJogo = []
    pontos = 0
    resetaJanela()
    #Imagens
    global imgTelaInicial #Definindo as variáveis como globais para funcionarem fora da estrutura da função
    global imgBotaoJogar
    global imgBotaoTutorial
    imgTelaInicial = PhotoImage(file='telas/telainicial.png')
    imgBotaoJogar = PhotoImage(file='botoes/botaojogar.png')
    imgBotaoTutorial = PhotoImage(file='botoes/botaotutorial.png')

    #Label
    labTelaInicial = Label(janela, image=imgTelaInicial)
    labTelaInicial.place(x=-2, y=-2)

    #Botões
    botaoJogar = Button(janela, bd=0, image=imgBotaoJogar, command=telaNome)
    botaoJogar.place(width=182, height=57, x=600, y=495)
    botaoTutorial = Button(janela, bd=0, image=imgBotaoTutorial, command=telaTutorial)
    botaoTutorial.place(width=182, height=57, x=600, y=585)

    #Colocando música de fundo
    pygame.init()
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load('musicas/musicapadrao.mp3')
    pygame.mixer.music.play(loops=-1)



#Função da tela de tutorial do jogo
def telaTutorial():
    resetaJanela()
    #Imagens
    global imgTelaTutorial #Definindo as variáveis como globais para funcionarem fora da estrutura da função
    global imgBotaoVoltar
    imgTelaTutorial = PhotoImage(file='telas/telatutorial.png')
    imgBotaoVoltar = PhotoImage(file='botoes/botaovoltar.png')

    #Label
    labTelaTutorial = Label(janela, image=imgTelaTutorial)
    labTelaTutorial.place(x=-2, y=-2)

    #Botões
    botaoVoltar = Button(janela, bd=0, image=imgBotaoVoltar, command=telaInicial)
    botaoVoltar.place(width=51, height=49, x=50, y=50)


#Função da tela de definição do nome do usuário
def telaNome():
    resetaJanela()
    #Imagens
    global imgTelaNome #Definindo as variáveis como globais para funcionarem fora da estrutura da função
    global imgBotaoVoltar
    global imgBotaoAvancar
    imgTelaNome = PhotoImage(file='telas/telanome.png')
    imgBotaoVoltar = PhotoImage(file='botoes/botaovoltar.png')
    imgBotaoAvancar = PhotoImage(file='botoes/botaoavancar.png')

    #Label
    labTelaNome = Label(janela, image=imgTelaNome)
    labTelaNome.place(x=-2, y=-2)

    #Botões
    botaoVoltar = Button(janela, bd=0, image=imgBotaoVoltar, command=telaInicial)
    botaoVoltar.place(width=51, height=49, x=50, y=50)
    botaoAvancar = Button(janela, bd=0, image=imgBotaoAvancar, command=testeNome)
    botaoAvancar.place(width=182, height=57, x=595, y=535)

    #Caixa de entrada
    global nomeUsuario
    nomeUsuario = Entry(janela, bd=5, bg='yellow', font=('Poppins Medium', 20), justify=CENTER)
    nomeUsuario.place(width=300, height=60, x=600, y=400)


#Função para testar se o nome digitado pelo usuário já existe nos rankings dos jogadores anteriores
def testeNome():
    global nome #Definindo as variáveis como globais para funcionarem fora da estrutura da função
    nome = nomeUsuario.get() #Puxando o nome do usuário que foi digitado na telaNome
    nome = nome.upper()

    nomeExiste = False
    for i in range(0, len(ranking)):
        testeRank = ranking[i].split(' ')
        if nome == testeRank[2] or (nome+'\n') == testeRank[2]:
            nomeExiste = True
    
    if nomeExiste == True:
        messagebox.showwarning('ATENÇÃO', 'Este nome de usuário já existe!')
    elif nome == '':
        messagebox.showwarning('ATENÇÃO', 'Digite algum nome de usuário!')
    elif  ' ' in nome:
        messagebox.showwarning('ATENÇÃO', 'Não use espaços no nome de usuário!')
    else:
        #Colocando música de fundo
        pygame.mixer.music.load('musicas/musicajogo.mp3')
        pygame.mixer.music.play(loops=-1)
        telaJogo()


#Função da tela de tempo caso o nível seja o Prodigio
def telaJogo():
    resetaJanela()
    global sequenciaJogo
    sequenciaJogo += [random.choice(alfabeto).upper()]
    #Imagens
    global imgTelaJogoProdigio #Definindo as variáveis como globais para funcionarem fora da estrutura da função
    global imgBotaoEnter
    global imgBotaoFechar
    imgBotaoFechar = PhotoImage(file='botoes/botaofechar.png')
    imgTelaJogoProdigio = PhotoImage(file='telas/telajogo.png')
    imgBotaoEnter = PhotoImage(file='botoes/botaoenter.png')

    #Label
    labTelaJogoProdigio = Label(janela, image=imgTelaJogoProdigio)
    labTelaJogoProdigio.place(x=-2, y=-2)
    labTextoJogo = Label(janela, fg='blue', bg='yellow', font=('Poppins Medium', 80), justify=CENTER, text=sequenciaJogo[-1], padx=20, pady=5)
    labTextoJogo.place(x=643, y=217)
    labTextoPonto = Label(janela, fg='blue', bg='yellow', font=('Poppins Medium', 30), justify=CENTER, text=pontos)
    labTextoPonto.place(x=1250, y=53)

    #Botões
    botaoEnter = Button(janela, bd=0, image=imgBotaoEnter, command=testeJogo)
    botaoEnter.place(width=130, height=72, x=635, y=510)
    botaoFechar = Button(janela, bd=0, image=imgBotaoFechar, command=telaInicial)
    botaoFechar.place(width=52, height=46, x=1285, y=676)

    #Caixa de entrada
    global letraJogo
    letraJogo = Entry(janela, bd=5, bg='yellow', font=('Poppins Medium', 20), justify=CENTER)
    letraJogo.place(width=400, height=60, x=498, y=420)
    
    #Colocando música de fundo


#Função que irá testar se a sequência do usuário bate com a sequência do jogo
def testeJogo():
    global pontos
    global sequenciaUsuario
    sequenciaUsuario = letraJogo.get()
    sequenciaUsuario = sequenciaUsuario.upper()
    sequenciaUsuario = list(sequenciaUsuario)
    if sequenciaUsuario == sequenciaJogo:
        pontos += 1
        telaJogo()
    else:
        telaGameOver()


#Função que direcionará para a tela de gameover
def telaGameOver():
    global pontos
    global sequenciaJogo
    global pontosFinal
    pontosFinal = pontos
    pontos = 0
    sequenciaJogo= []
    resetaJanela()
    global imgTelaGameOver #Definindo as variáveis como globais para funcionarem fora da estrutura da função
    global imgBotaoRanking
    global imgBotaoJogarNovamente
    imgTelaGameOver = PhotoImage(file='telas/telagameover.png')
    imgBotaoRanking = PhotoImage(file='botoes/botaoranking.png')
    imgBotaoJogarNovamente = PhotoImage(file='botoes/botaojogarnovamente.png')

    #Label
    labTelaGameOver = Label(janela, image=imgTelaGameOver)
    labTelaGameOver.place(x=-2, y=-2)
    labTextoPontoFinal = Label(janela, fg='blue', bg='yellow', font=('Poppins Medium', 40), justify=CENTER, text=pontosFinal)
    labTextoPontoFinal.place(x=683, y=480)

    #Botões
    botaoRanking = Button(janela, bd=0, image=imgBotaoRanking, command=telaRanking)
    botaoRanking.place(width=181, height=55, x=612, y=600)
    botaoJogarNovamente = Button(janela, bd=0, image=imgBotaoJogarNovamente, command=testeNome)
    botaoJogarNovamente.place(width=306, height=55, x=549, y=675)

    #Colocando música de fundo
    pygame.mixer.music.load('musicas/musicagameover.mp3')
    pygame.mixer.music.play(loops=1)


#Função para levar para a tela de ranking e mostrar a classificação
def telaRanking():
    salvarRanking()
    #Imagens
    global imgTelaRanking #Definindo as variáveis como globais para funcionarem fora da estrutura da função
    global imgBotaoSair
    global labJogador1
    global labJogador2
    global labJogador3
    global labJogador4
    global labJogador5
    imgTelaRanking = PhotoImage(file='telas/telaranking.png')
    imgBotaoSair = PhotoImage(file='botoes/botaofechar.png')

    #Label
    labTelaRanking = Label(janela, image=imgTelaRanking)
    labTelaRanking.place(x=-2, y=-2)
    if len(ranking) >= 1:
        if '\n' in ranking[0]:
            primeiroLugar = ranking[0][0:-1]
        else:
            primeiroLugar = ranking[0]
        labJogador1 = Label(janela, fg='blue', bg='yellow', font=('Poppins Medium', 20), justify=CENTER, text=primeiroLugar)
        labJogador1.place(x=260, y=267)
    if len(ranking) >= 2:
        if '\n' in ranking[1]:
            segundoLugar = ranking[1][0:-1]
        else:
            segundoLugar = ranking[1]
        labJogador2 = Label(janela, fg='blue', bg='yellow', font=('Poppins Medium', 20), justify=CENTER, text=segundoLugar)
        labJogador2.place(x=260, y=410)
    if len(ranking) >= 3:
        if '\n' in ranking[2]:
            terceiroLugar = ranking[2][0:-1]
        else:
            terceiroLugar = ranking[2]
        labJogador3 = Label(janela, fg='blue', bg='yellow', font=('Poppins Medium', 20), justify=CENTER, text=terceiroLugar)
        labJogador3.place(x=260, y=547)
    if len(ranking) >= 4:
        if '\n' in ranking[3]:
            quartoLugar = ranking[3][0:-1]
        else:
            quartoLugar = ranking[3]
        labJogador4 = Label(janela, fg='blue', bg='yellow', font=('Poppins Medium', 20), justify=CENTER, text=quartoLugar)
        labJogador4.place(x=915, y=313)
    if len(ranking) >= 5:
        if '\n' in ranking[4]:
            quintoLugar = ranking[4][0:-1]
        else:
            quintoLugar = ranking[4]
        labJogador5 = Label(janela, fg='blue', bg='yellow', font=('Poppins Medium', 20), justify=CENTER, text=quintoLugar)
        labJogador5.place(x=915, y=455)

    #Botões
    botaoSair = Button(janela, bd=0, image=imgBotaoSair, command=telaInicial)
    botaoSair.place(width=51, height=49, x=50, y=50)

    #Colocando música de fundo
    pygame.mixer.music.load('musicas/musicaranking.mp3')
    pygame.mixer.music.play(loops=-1)


#Função para preencher o arquivo txt do ranking
def salvarRanking():
    global pontosFinal
    global ranking
    if pontosFinal < 10:
        pontosFinal = '0' + str(pontosFinal)
    ranking += [str(pontosFinal) + ' - ' + nome]

    bolha(ranking)

    rankingArquivo = open('ranking.txt', 'w')
    for i in range(0, len(ranking)):
        rank = ranking[i]
        if rank[0] in '0123456789':
            rankingArquivo.write(rank)
            rankingArquivo.write('\n')
    rankingArquivo.close()


#Chamando a função da tela inicial para dar início ao jogo
telaInicial()
#Após isso o funcionamento do código será "pulando" de função em função

#Código do Tkinter que deixa a tela rodando, sem ele a tela abriria e fecharia "instantaneamente"
janela.mainloop()
