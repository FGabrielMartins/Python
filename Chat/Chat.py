# Titulo: Bate-papo
# botão de iniciar chat 
    # Clicou no botão:
        # Popup/Modal (janela)
            # Título: bem vindo >>>
            # Campo: escreva seu nome no chat
            #botão: entrar no chat
# Chat
# embaixo do chat
    # Campo de digite sua mensgem
    # Botão de enviar

# flet -> framework do python // pip install flet
# copilar a força// python chat.py

import flet as ft

def main(pagina): # Criar a finção principal
    texto = ft.Text("Bate Papo")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        print(mensagem)
         # Adicione a mensagem no chat
        texto_de_entrada = ft.Text(mensagem)
        chat.controls.append(texto_de_entrada)
        pagina.update()

        pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem (evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        # limpe o campo mensagem
        campo_mensagem.value = ""

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    campo_mensagem =  ft.TextField(label = "DIgite sua mensagem", on_submit= enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click = enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        print("Entrar no chat")
        # Fechar o popup
        popup.open = False
        # Tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # Tirar o título
        pagina.remove(texto)
        # Criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        # Colocar campo de digitar o chat
        pagina.add(linha_enviar)
        # Criar o botão de enviar

        pagina.update()

    titulo_popup = ft.Text("Bem vinda Roberta")
    nome_usuario = ft.TextField(label="Escreca seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(open=False, modal=True, title=titulo_popup, content=nome_usuario, actions=[botao_entrar])
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click = abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)
ft.app(target=main, view=ft.WEB_BROWSER) # Criar o app chamando a função principal