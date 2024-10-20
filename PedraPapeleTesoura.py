import random
import tkinter as tk
from tkinter import messagebox
import emoji

#Feito para ser um aquivo.exe
# Função do jogo
def jogar(escolha_jogador):
    pedra = 'pedra'
    papel = 'papel'
    tesoura = 'tesoura'
    lista = [pedra, papel, tesoura]
    escolha_computador = random.choice(lista)
    
    # Exibir as escolhas
    resultado = f"Você escolheu {escolha_jogador}\nComputador escolheu {escolha_computador}\n"

    # Lógica do jogo
    if escolha_computador == escolha_jogador:
        resultado += "Resultado: Empate!"
    elif (escolha_computador == pedra and escolha_jogador == papel) or \
         (escolha_computador == papel and escolha_jogador == tesoura) or \
         (escolha_computador == tesoura and escolha_jogador == pedra):
        resultado += "Resultado: Você ganhou!"
    else:
        resultado += "Resultado: Você perdeu!"

    # Atualizar o label de resultado
    resultado_label.config(text=resultado)

# Configuração da janela
janela = tk.Tk()
janela.title("Jogo Pedra, Papel e Tesoura")
janela.geometry("400x350")

# Texto de instrução
instrucao_label = tk.Label(janela, text="Escolha Pedra, Papel ou Tesoura:", font=("Helvetica", 14))
instrucao_label.pack(pady=10)

# Botões de escolha
button_pedra = tk.Button(janela, text=emoji.emojize(":gem_stone: Pedra"), font=("Helvetica", 12),
                         command=lambda: jogar("pedra"))
button_pedra.pack(pady=5)

button_papel = tk.Button(janela, text=emoji.emojize(":roll_of_paper: Papel"), font=("Helvetica", 12),
                         command=lambda: jogar("papel"))
button_papel.pack(pady=5)

button_tesoura = tk.Button(janela, text=emoji.emojize(":scissors: Tesoura"), font=("Helvetica", 12),
                           command=lambda: jogar("tesoura"))
button_tesoura.pack(pady=5)

# Label para exibir o resultado
resultado_label = tk.Label(janela, text="", font=("Helvetica", 12), wraplength=300, justify="center")
resultado_label.pack(pady=20)

# Rodapé
rodape_label = tk.Label(janela, text="Copyright © 2024 - by DaviFoundation", font=("Helvetica", 8), fg="gray")
rodape_label.pack(side="bottom", pady=10)

# Iniciar a interface
janela.mainloop()
