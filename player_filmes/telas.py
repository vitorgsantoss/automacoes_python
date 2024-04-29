import tkinter as tk
from save_password import save_date
from seach_film import search


def login(): 
    def enviar_credenciais():
        email = entry_email.get()
        password = entry_senha.get()
        
        save_date(email, password)
        janela.destroy()

   
    janela = tk.Tk()
    janela.title("Login")

    label_email = tk.Label(janela, text="Email:")
    label_email.grid(row=0, column=0, padx=10, pady=5)
    entry_email = tk.Entry(janela)
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    label_senha = tk.Label(janela, text="Senha:")
    label_senha.grid(row=1, column=0, padx=10, pady=5)
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.grid(row=1, column=1, padx=10, pady=5)


    botao_enviar = tk.Button(janela, text="Enviar", command=enviar_credenciais)
    botao_enviar.grid(row=2, column=0, columnspan=2, pady=10)

    janela.mainloop()

def filmOrSerie(email, password):
    def buscar():
        tempo_sem_espaço = entry_tempo.get().strip()
        if tempo_sem_espaço.isdigit():
            tempo= int(tempo_sem_espaço)
            tempo_em_segundos = tempo * 60
        janela.withdraw()
        search(entry_filme.get(), email, password, tempo_em_segundos)
           
    janela = tk.Tk()
    janela.title("Informe o Filme")

    label_filme = tk.Label(janela, text="Filme ou Série:")
    label_filme.grid(row=0, column=0, padx=10, pady=5)
    entry_filme = tk.Entry(janela)
    entry_filme.grid(row=0, column=1, padx=10, pady=5)

    label_tempo = tk.Label(janela, text="Informe o tempo que deseja assistir (minutos):")
    label_tempo.grid(row=1, column=0, padx=10, pady=5)
    entry_tempo = tk.Entry(janela)
    entry_tempo.grid(row=1, column=1, padx=10, pady=5)

    

    botao_enviar = tk.Button(janela, text="Enviar", command=buscar)
    botao_enviar.grid(row=2, column=0, columnspan=2, pady=10)

    janela.mainloop()