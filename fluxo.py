import sqlite3
import tkinter as tk
from tkinter import messagebox


conexao = sqlite3.connect("pagamentos.db")
cursor = conexao.cursor()

#Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS pagamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    descricao TEXT,
    beneficiario TEXT,
    data TEXT,
    valor REAL,
    status TEXT
)
""")

conexao.commit()

#Funcao para cadastrar um titulo
def cadastrar():
    tipo = entrada_tipo.get()
    descricao = entrada_descricao.get()
    beneficiario = entrada_beneficiario.get()
    data = entrada_data.get()
    valor = entrada_valor.get()
    status = entrada_status.get()

    cursor.execute("""
    INSERT INTO pagamentos (tipo, descricao, beneficiario, data, valor, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (tipo, descricao, beneficiario, data, valor, status))

    conexao.commit()
    messagebox.showinfo("Sucesso", "Título cadastrado com sucesso!")

#Funcao para listar os titulos
def listar():
    cursor.execute("SELECT * FROM pagamentos")
    registros = cursor.fetchall()
    texto_lista.delete("1.0", tk.END) #limpa a area de texto antes de mostrar a lista atualizada
    for r in registros:
        texto_lista.insert(tk.END, f"{r}\n")

#Funcao para atualizar um titulo
def atualizar():
    id_titulo = entrada_id.get()
    novo_status = entrada_status.get()
    cursor.execute("UPDATE pagamentos SET status = ? WHERE id = ?", (novo_status, id_titulo))
    conexao.commit()
    messagebox.showinfo("Sucesso", "Título atualizado com sucesso!")

#Funcao para excluir um titulo
def excluir():
    id_titulo = entrada_id.get()
    cursor.execute("DELETE FROM pagamentos WHERE id = ?", (id_titulo,))
    conexao.commit()
    messagebox.showinfo("Sucesso", "Título excluído com sucesso!")


#Janela principal
janela = tk.Tk()
janela.title("Controle de Pagamentos")
janela.geometry("400x300")
janela.configure(bg="#414040")


#Campos de entrada
tk.Label(janela, bg="#FFFFFF", text="Tipo (a pagar/a receber):").grid(row=0, column=0)
entrada_tipo = tk.Entry(janela)
entrada_tipo.grid(row=0, column=1)

tk.Label(janela, text="Descrição:").grid(row=1, column=0)
entrada_descricao = tk.Entry(janela)
entrada_descricao.grid(row=1, column=1)

tk.Label(janela, text="Beneficiário:").grid(row=2, column=0)
entrada_beneficiario = tk.Entry(janela)
entrada_beneficiario.grid(row=2, column=1)

tk.Label(janela, text="Valor:").grid(row=3, column=0)
entrada_valor = tk.Entry(janela)
entrada_valor.grid(row=3, column=1)

tk.Label(janela, text="Data (dd/mm/aaaa):").grid(row=4, column=0)
entrada_data = tk.Entry(janela)
entrada_data.grid(row=4, column=1)

tk.Label(janela, text="Status (pendente/pago):").grid(row=5, column=0)
entrada_status = tk.Entry(janela)
entrada_status.grid(row=5, column=1)

tk.Label(janela, text="ID (para atualizar/excluir):").grid(row=6, column=0)
entrada_id = tk.Entry(janela)
entrada_id.grid(row=6, column=1)

#Botões de ação
tk.Button(janela, text="Cadastrar", bg="#008000", fg="white", command=cadastrar).grid(row=7, column=0)
tk.Button(janela, text="Listar", bg="#0000FF", fg="white", command=listar).grid(row=7, column=1)
tk.Button(janela, text="Atualizar", bg="#FFA500", fg="white", command=atualizar).grid(row=8, column=0)
tk.Button(janela, text="Excluir", bg="#FF0000", fg="white", command=excluir).grid(row=8, column=1)

#Area de texto pera mostrar lista
texto_lista = tk.Text(janela, bg="#76CCDD" , height=10, width=50)
texto_lista.grid(row=9, column=0, columnspan=2)



#Iniciar a interface
janela.mainloop()

#Fechar conexao
conexao.close()