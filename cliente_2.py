
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Trabalhando com recebimento de mensagem """
    while True:
        try:
            mensagem = client_socket.recv(BUFSIZ).decode("utf8")
            mensagem_split = mensagem.split("@")
            print(mensagem_split)
            if len(mensagem_split) > 1:
                destino = mensagem_split[1]
                print(destino)
                if destino == my_name.get():
                    print(mensagem_split)
                    mensagem_list.insert(
                        tkinter.END, "By: " + mensagem_split[0])
                    mensagem_list.insert(
                        tkinter.END, "Assunto: " + mensagem_split[2])
                    mensagem_list.insert(
                        tkinter.END, "Mensagem: " + mensagem_split[3])
                    mensagem_list.insert(tkinter.END, " ")

            if len(mensagem_split) == 1:
                mensagem_list.insert(tkinter.END, mensagem)
                print(mensagem)

        except OSError:  # Possivelmente o cliente saiu do chat
            break


def send_name(event=None):  # evento é passado por ligação.
    """Lida com o envio de mensagens."""
    mensagem = my_name.get()
    print(mensagem)
    client_socket.send(bytes(mensagem, "utf8"))


def send(event=None):  # evento é passado por ligação.
    """Lida com o envio de mensagens."""
    if my_destinatario.get() != "" and my_mensagem.get() != "":
        mensagem = "@" + my_destinatario.get() + "@" + my_assunto.get() + \
            "@" + my_mensagem.get()
        my_destinatario.set("")  # Limpa o campo de entrada.
        my_assunto.set("")
        my_mensagem.set("")  # Limpa o campo de entrada.
        client_socket.send(bytes(mensagem, "utf8"))


def sair(event=None):  # evento é passado por ligação.
    """Encerrar a conexão"""
    mensagem = "{quit}"
    client_socket.send(bytes(mensagem, "utf8"))
    client_socket.close()
    janela.quit()


def on_closing(event=None):
    """Esta função é chamada quando a janela é fechada."""
    my_mensagem.set("{quit}")
    send()


janela = tkinter.Tk()
janela.title("CLiente_2")
janela.configure(bg="#E6E6FA")
janela.geometry("+0+10")
janela.iconbitmap(default="icon/original.ico")
janela.resizable(width=False, height=False)


messages_frame = tkinter.Frame(janela)
my_name = tkinter.StringVar()
my_destinatario = tkinter.StringVar()
my_assunto = tkinter.StringVar()
my_mensagem = tkinter.StringVar()  # Para que as mensagens sejam enviada

scrollbar = tkinter.Scrollbar(messages_frame)

l_seu_nome = tkinter.Label(janela, text="Seu nome:",
                           font="Verdana 16 bold", width=11, height=2, bg="#E6E6FA")
l_destinatario = tkinter.Label(
    janela, text=" Destinatário:", font="Verdana 16 bold", width=11, height=2, bg="#E6E6FA")
l_assunto = tkinter.Label(janela, text="       Assunto:",
                          font="Verdana 16 bold", width=11, height=1, bg="#E6E6FA")
l_mensagem = tkinter.Label(janela, text="   Mensagem:",
                           font="Verdana 16 bold", width=11, height=2, bg="#E6E6FA")

l_caixa_de_entrada = tkinter.Label(
    janela, text="Caixa de Entrada", font="Verdana 16 bold", height=1, bg="#E6E6FA")

l_divisoriac = tkinter.Label(janela, width=1, height=1, bg="#4B0082")
l_divisorian = tkinter.Label(janela, width=1, height=1, bg="#4B0082")
l_divisorias = tkinter.Label(janela, width=1, height=1, bg="#4B0082")
l_divisoriae = tkinter.Label(janela, width=1, height=1, bg="#4B0082")
l_divisoriaw = tkinter.Label(janela, width=1, height=1, bg="#4B0082")

mensagem_list = tkinter.Listbox(janela, height=11, width=38, font="Verdana 12 bold", fg="#4B0082", border=2,
                                yscrollcommand=scrollbar.set)

e_seu_nome = tkinter.Entry(
    janela, font="Verdana 12 bold", fg="#4B0082", textvariable=my_name)
e_seu_nome.bind("<Return>", )
e_destinatario = tkinter.Entry(
    janela, font="Verdana 12 bold", fg="#4B0082", textvariable=my_destinatario)
e_destinatario.bind("<Return>", )
e_assunto = tkinter.Entry(janela, font="verdana 12 bold",
                          fg="#4B0082", textvariable=my_assunto)
e_assunto.bind("<Return>", )
e_mensagem = tkinter.Entry(
    janela, font="Verdana 12 bold", fg="#4B0082", textvariable=my_mensagem)
e_mensagem.bind("<Return>", )

janela.protocol("WM_DELETE_WINDOW", on_closing)

b_enviar_nome = tkinter.Button(janela, text="    Enviar Nome    ", font="Verdana 14 bold", height=1, border=3,
                               relief="groove", fg="#4B0082", command=send_name)
b_enviar = tkinter.Button(janela, text="Enviar Mensagem", font="Verdana 14 bold", height=1, border=3,
                          relief="groove", fg="#4B0082", command=send)
b_sair = tkinter.Button(janela, text="Sair", font="Verdana 14 bold", fg="#B22222", border=3, relief='groove',
                        command=sair)

scrollbar.grid()
mensagem_list.grid(row=10, column=1, columnspan=2)
messages_frame.grid()

l_divisorian.grid(row=0, column=0, columnspan=3, sticky="e"+"w")
l_divisorias.grid(row=13, column=0, columnspan=3, sticky="e"+"w")
l_divisoriae.grid(row=0, column=0, rowspan=13, sticky="n"+"s")
l_divisoriaw.grid(row=0, column=3, rowspan=14, sticky="n"+"s")

l_seu_nome.grid(row=1, column=1, sticky="w")
l_destinatario.grid(row=3, column=1, sticky="w")
l_assunto.grid(row=4, column=1, sticky="w")
l_mensagem.grid(row=5, column=1, sticky="w")
l_divisoriac.grid(row=8, column=1)
l_caixa_de_entrada.grid(row=9, column=1, columnspan=3)

e_seu_nome.grid(row=1, column=2)
e_destinatario.grid(row=3, column=2)
e_assunto.grid(row=4, column=2)
e_mensagem.grid(row=5, column=2)


b_enviar.grid(row=6, column=2, sticky="n")
b_enviar_nome.grid(row=2, column=2, sticky="n")
b_sair.grid(row=12, column=1, columnspan=3)


HOST = "localhost"
PORT = 33000
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
# Inicia a execução da GUI.
janela.mainloop()
