import tkinter as tk
from tkinter import messagebox
import json
import os
from tkinter import simpledialog

# Arquivos para salvar os dados
ARQUIVO_AGUA = "historico_contas_agua.json"  # Arquivo para salvar o histórico de contas de água
ARQUIVO_ENERGIA = "historico_contas_energia.json"  # Arquivo para salvar o histórico de contas de energia

# Dicionários para armazenar os dados
historico_agua = {}  # Dicionário para armazenar as contas de água por mês/ano
historico_energia = {}  # Dicionário para armazenar as contas de energia por mês/ano

# Função para carregar os dados dos arquivos JSON
def carregar_dados():
    global historico_agua, historico_energia
    # Verifica se o arquivo de água existe, e carrega os dados
    if os.path.exists(ARQUIVO_AGUA):
        with open(ARQUIVO_AGUA, "r") as arquivo:
            historico_agua.update(json.load(arquivo))  # Atualiza o dicionário com os dados carregados
    # Verifica se o arquivo de energia existe, e carrega os dados
    if os.path.exists(ARQUIVO_ENERGIA):
        with open(ARQUIVO_ENERGIA, "r") as arquivo:
            historico_energia.update(json.load(arquivo))  # Atualiza o dicionário com os dados carregados
    atualizar_leaderboards()  # Atualiza a exibição dos históricos de contas

# Função para salvar os dados nos arquivos JSON
def salvar_dados():
    # Salva os dados de água no arquivo JSON
    with open(ARQUIVO_AGUA, "w") as arquivo:
        json.dump(historico_agua, arquivo)
    # Salva os dados de energia no arquivo JSON
    with open(ARQUIVO_ENERGIA, "w") as arquivo:
        json.dump(historico_energia, arquivo)

# Função para atualizar os leaderboards na interface gráfica
def atualizar_leaderboards():
    # Limpa a lista de leaderboard de água e atualiza com os dados
    leaderboard_agua.delete(0, tk.END)
    for mes_ano, valor in sorted(historico_agua.items(), key=lambda x: x[1], reverse=True):
        leaderboard_agua.insert(tk.END, f"{mes_ano}: R$ {valor:.2f}")  # Exibe o valor de cada mês/ano em ordem decrescente
    
    # Limpa a lista de leaderboard de energia e atualiza com os dados
    leaderboard_energia.delete(0, tk.END)
    for mes_ano, valor in sorted(historico_energia.items(), key=lambda x: x[1], reverse=True):
        leaderboard_energia.insert(tk.END, f"{mes_ano}: R$ {valor:.2f}")  # Exibe o valor de cada mês/ano em ordem decrescente

# Função para salvar o valor da conta de água
def salvar_mes_agua(mes_ano, valor_total):
    # Verifica se o mês já foi registrado, e se sim, exibe um erro
    if mes_ano in historico_agua:
        messagebox.showerror("Erro", f"O mês {mes_ano} já foi registrado para água. Por favor, edite ou use outro mês.")
        return
    # Salva o valor da conta para o mês/ano no histórico
    historico_agua[mes_ano] = valor_total
    salvar_dados()  # Salva os dados no arquivo
    atualizar_leaderboards()  # Atualiza os leaderboards

# Função para salvar o valor da conta de energia
def salvar_mes_energia(mes_ano, valor_total):
    # Verifica se o mês já foi registrado, e se sim, exibe um erro
    if mes_ano in historico_energia:
        messagebox.showerror("Erro", f"O mês {mes_ano} já foi registrado para energia. Por favor, edite ou use outro mês.")
        return
    # Salva o valor da conta para o mês/ano no histórico
    historico_energia[mes_ano] = valor_total
    salvar_dados()  # Salva os dados no arquivo
    atualizar_leaderboards()  # Atualiza os leaderboards

# Função para mostrar dicas sobre como economizar água
def dicas_agua():
    # Cria a mensagem de dicas sobre economia de água
    dica = "Dicas para economizar água:\n"
    dica += "- Tome banhos mais rápidos.\n"
    dica += "- Feche a torneira ao escovar os dentes.\n"
    dica += "- Reutilize a água sempre que possível (por exemplo, para limpeza)."
    # Exibe as dicas em uma caixa de mensagem
    messagebox.showinfo("Dicas de Economia de Água", dica)

# Função para mostrar dicas sobre como economizar energia
def dicas_energia():
    # Cria a mensagem de dicas sobre economia de energia
    dica = "Dicas para economizar energia:\n"
    dica += "- Desligue aparelhos eletrônicos quando não estiverem em uso.\n"
    dica += "- Utilize lâmpadas LED, que consomem menos energia.\n"
    dica += "- Aproveite a luz natural sempre que possível."
    # Exibe as dicas em uma caixa de mensagem
    messagebox.showinfo("Dicas de Economia de Energia", dica)

# Função para calcular o valor da conta de água
def calcular_agua():
    try:
        # Obtém os valores de consumo, tarifa, taxa de esgoto e taxa fixa a partir da interface gráfica
        consumo = float(entry_consumo_agua.get())  # Consumo em metros cúbicos
        tarifa = float(entry_tarifa_agua.get())  # Tarifa por metro cúbico
        taxa_esgoto = float(entry_taxa_esgoto.get())  # Taxa de esgoto em %
        taxa_fixa = float(entry_taxa_fixa_agua.get())  # Taxa fixa (valores adicionais)
        mes = entry_mes_agua.get().strip()  # Mês em que a conta será registrada
        ano = entry_ano_agua.get().strip()  # Ano em que a conta será registrada

        # Verifica se os campos de mês e ano foram preenchidos
        if not mes or not ano:
            messagebox.showerror("Erro", "Por favor, insira o mês e o ano.")
            return

        mes_ano = f"{mes}/{ano}"  # Formato mês/ano

        # Calcula o valor da conta de água
        valor_agua = consumo * tarifa  # Valor do consumo de água
        valor_esgoto = valor_agua * (taxa_esgoto / 100)  # Calcula a taxa de esgoto sobre o valor do consumo
        valor_total = valor_agua + valor_esgoto + taxa_fixa  # Valor total considerando o consumo, esgoto e taxa fixa

        # Salva o valor total no histórico de água
        salvar_mes_agua(mes_ano, valor_total)

        # Exibe o valor total da conta de água e o consumo em litros
        messagebox.showinfo(f"Conta de Água de {mes_ano}", f"Valor total: R$ {valor_total:.2f}\nConsumo em litros: {consumo*1000:.0f}")
        dicas_agua()  # Mostra dicas sobre economia de água

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos (use ponto no lugar da vírgula).")

# Função para calcular o valor da conta de energia
def calcular_energia():
    try:
        # Obtém os valores de consumo, tarifa, ICMS, encargos, mês, ano e bandeira tarifária
        consumo = float(entry_consumo_energia.get())  # Consumo em kWh
        tarifa = float(entry_tarifa_energia.get())  # Tarifa por kWh
        icms = float(entry_icms.get())  # ICMS em %
        encargos = float(entry_encargos.get())  # Encargos adicionais
        mes = entry_mes_energia.get().strip()  # Mês
        ano = entry_ano_energia.get().strip()  # Ano
        bandeira = entry_bandeira_energia.get().strip().lower()  # Bandeira tarifária (verde, amarela, vermelha_1, vermelha_2)

        # Verifica se os campos de mês e ano foram preenchidos
        if not mes or not ano:
            messagebox.showerror("Erro", "Por favor, insira o mês e o ano.")
            return
        
        # Verifica se a bandeira é válida
        if bandeira not in ["verde", "amarela", "vermelha_1", "vermelha_2"]:
            messagebox.showerror("Erro", "Por favor, insira uma bandeira válida (verde, amarela, vermelha_1, vermelha_2).")
            return

        # Dicionário com os valores das bandeiras tarifárias
        bandeiras = {
            "verde": 0.00,  # Bandeira verde: sem acréscimo
            "amarela": 0.05,  # Bandeira amarela: R$ 0,05/kWh
            "vermelha_1": 0.10,  # Bandeira vermelha - Patamar 1: R$ 0,10/kWh
            "vermelha_2": 0.20   # Bandeira vermelha - Patamar 2: R$ 0,20/kWh
        }
        
        # Calcula o valor do consumo de energia sem a bandeira
        valor_consumo = consumo * tarifa
        
        # Aplica o valor da bandeira ao consumo de energia
        valor_bandeira = consumo * bandeiras[bandeira]
        
        # Calcula o ICMS sobre o valor do consumo
        valor_icms = valor_consumo * (icms / 100)
        
        # Calcula o valor total da conta, incluindo a bandeira e ICMS
        valor_total = valor_consumo + valor_bandeira + valor_icms + encargos

        mes_ano = f"{mes}/{ano}"  # Formato mês/ano

        # Salva o valor total da conta de energia
        salvar_mes_energia(mes_ano, valor_total)
        
        # Exibe o valor total da conta de energia
        messagebox.showinfo(f"Conta de Energia de {mes_ano}", f"Valor total: R$ {valor_total:.2f}")
        dicas_energia()  # Mostra dicas sobre economia de energia
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos (use ponto no lugar da vírgula).")

# Função para editar o valor de um mês específico no histórico
def editar_mes(lista, tipo):
    selecionado = lista.curselection()  # Obtém o item selecionado na lista
    if selecionado:
        item = lista.get(selecionado[0])  # Pega o item da lista
        mes_ano, _ = item.split(":")  # Extrai o mês/ano
        novo_valor = simpledialog.askstring("Editar", f"Novo valor para {mes_ano} (R$):")  # Pede o novo valor ao usuário
        if novo_valor:
            try:
                novo_valor = float(novo_valor)  # Converte o novo valor para float
                
                # Verifica se o tipo é 'agua' ou 'energia' e seleciona o histórico correto
                if tipo == "agua":
                    historico = historico_agua
                elif tipo == "energia":
                    historico = historico_energia
                else:
                    return
                
                # Verifica se o mês/ano existe no histórico
                if mes_ano.strip() not in historico:
                    messagebox.showerror("Erro", f"Erro ao localizar o mês {mes_ano}.")
                    return

                # Atualiza o valor do mês/ano no histórico
                historico[mes_ano.strip()] = novo_valor
                salvar_dados()  # Salva os dados atualizados
                atualizar_leaderboards()  # Atualiza os leaderboards
                messagebox.showinfo("Sucesso", f"O mês {mes_ano} foi atualizado com sucesso.")
            except ValueError:
                messagebox.showerror("Erro", "Insira um valor numérico válido.")  # Caso o valor inserido não seja válido
    else:
        messagebox.showerror("Erro", "Por favor, selecione um item para editar.")  # Caso nenhum item seja selecionado

# Função para deletar um mês específico do histórico
def deletar_mes(lista, tipo):
    selecionado = lista.curselection()  # Obtém o item selecionado da lista
    if selecionado:
        item = lista.get(selecionado[0])  # Pega o item da lista
        mes_ano, _ = item.split(":")  # Extrai o mês/ano do item selecionado
        # Pergunta ao usuário se tem certeza que quer deletar o item
        if messagebox.askyesno("Confirmação", f"Tem certeza que deseja deletar {mes_ano}?"):
            if tipo == "agua":  # Se for do tipo "agua", deleta do histórico de água
                del historico_agua[mes_ano.strip()]
            elif tipo == "energia":  # Se for do tipo "energia", deleta do histórico de energia
                del historico_energia[mes_ano.strip()]
            salvar_dados()  # Salva as alterações
            atualizar_leaderboards()  # Atualiza os leaderboards
    else:
        messagebox.showerror("Erro", "Por favor, selecione um item para deletar.")  # Se nenhum item for selecionado

# Interface gráfica
root = tk.Tk()  # Criação da janela principal
root.title("EcoBrasil")  # Título da janela

# Seção para Água
frame_agua = tk.LabelFrame(root, text="Conta de Água", padx=10, pady=10)  # Criação do frame para água
frame_agua.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Campos de entrada para dados de água
tk.Label(frame_agua, text="Consumo (m³):").grid(row=0, column=0, sticky="w")
entry_consumo_agua = tk.Entry(frame_agua)
entry_consumo_agua.grid(row=0, column=1)

tk.Label(frame_agua, text="Tarifa (R$/m³):").grid(row=1, column=0, sticky="w")
entry_tarifa_agua = tk.Entry(frame_agua)
entry_tarifa_agua.grid(row=1, column=1)

tk.Label(frame_agua, text="Taxa de Esgoto (%):").grid(row=2, column=0, sticky="w")
entry_taxa_esgoto = tk.Entry(frame_agua)
entry_taxa_esgoto.grid(row=2, column=1)

tk.Label(frame_agua, text="Taxa Fixa (R$):").grid(row=3, column=0, sticky="w")
entry_taxa_fixa_agua = tk.Entry(frame_agua)
entry_taxa_fixa_agua.grid(row=3, column=1)

tk.Label(frame_agua, text="Mês:").grid(row=4, column=0, sticky="w")
entry_mes_agua = tk.Entry(frame_agua)
entry_mes_agua.grid(row=4, column=1)

tk.Label(frame_agua, text="Ano:").grid(row=5, column=0, sticky="w")
entry_ano_agua = tk.Entry(frame_agua)
entry_ano_agua.grid(row=5, column=1)

# Botão para calcular a conta de água
btn_calcular_agua = tk.Button(frame_agua, text="Calcular Conta de Água", command=calcular_agua)
btn_calcular_agua.grid(row=6, columnspan=2, pady=10)

# Lista para exibir os históricos de conta de água
leaderboard_agua = tk.Listbox(frame_agua, height=10, width=40)
leaderboard_agua.grid(row=7, columnspan=2, pady=10)

# Botões para editar ou deletar o histórico de água
btn_editar_agua = tk.Button(frame_agua, text="Editar Selecionado", command=lambda: editar_mes(leaderboard_agua, "agua"))
btn_editar_agua.grid(row=8, column=0)

btn_deletar_agua = tk.Button(frame_agua, text="Deletar Selecionado", command=lambda: deletar_mes(leaderboard_agua, "agua"))
btn_deletar_agua.grid(row=8, column=1)

# Seção para Energia
frame_energia = tk.LabelFrame(root, text="Conta de Energia", padx=10, pady=10)  # Criação do frame para energia
frame_energia.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Campos de entrada para dados de energia
tk.Label(frame_energia, text="Consumo (kWh):").grid(row=0, column=0, sticky="w")
entry_consumo_energia = tk.Entry(frame_energia)
entry_consumo_energia.grid(row=0, column=1)

tk.Label(frame_energia, text="Tarifa (R$/kWh):").grid(row=1, column=0, sticky="w")
entry_tarifa_energia = tk.Entry(frame_energia)
entry_tarifa_energia.grid(row=1, column=1)

tk.Label(frame_energia, text="ICMS (%):").grid(row=2, column=0, sticky="w")
entry_icms = tk.Entry(frame_energia)
entry_icms.grid(row=2, column=1)

tk.Label(frame_energia, text="Encargos (R$):").grid(row=3, column=0, sticky="w")
entry_encargos = tk.Entry(frame_energia)
entry_encargos.grid(row=3, column=1)

tk.Label(frame_energia, text="Bandeira:").grid(row=4, column=0, sticky="w")
entry_bandeira_energia = tk.Entry(frame_energia)
entry_bandeira_energia.grid(row=4, column=1)

tk.Label(frame_energia, text="Mês:").grid(row=5, column=0, sticky="w")
entry_mes_energia = tk.Entry(frame_energia)
entry_mes_energia.grid(row=5, column=1)

tk.Label(frame_energia, text="Ano:").grid(row=6, column=0, sticky="w")
entry_ano_energia = tk.Entry(frame_energia)
entry_ano_energia.grid(row=6, column=1)

# Botão para calcular a conta de energia
btn_calcular_energia = tk.Button(frame_energia, text="Calcular Conta de Energia", command=calcular_energia)
btn_calcular_energia.grid(row=7, columnspan=2, pady=10)

# Lista para exibir os históricos de conta de energia
leaderboard_energia = tk.Listbox(frame_energia, height=10, width=40)
leaderboard_energia.grid(row=8, columnspan=2, pady=10)

# Botões para editar ou deletar o histórico de energia
btn_editar_energia = tk.Button(frame_energia, text="Editar Selecionado", command=lambda: editar_mes(leaderboard_energia, "energia"))
btn_editar_energia.grid(row=9, column=0)

btn_deletar_energia = tk.Button(frame_energia, text="Deletar Selecionado", command=lambda: deletar_mes(leaderboard_energia, "energia"))
btn_deletar_energia.grid(row=9, column=1)

# Função para carregar os dados ao iniciar
carregar_dados()

# Inicia o loop da interface gráfica
root.mainloop()