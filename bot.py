import discord
import io
import os
from rembg import remove
from PIL import Image

# =============================================
# CONFIGURAÇÃO — coloque seu token aqui
# =============================================
TOKEN = os.getenv("DISCORD_TOKEN")  # Pega do ambiente (Railway/Render)

# =============================================
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"✅ Bot online como {client.user}")


@client.event
async def on_message(message):
    # Ignora mensagens do próprio bot
    if message.author == client.user:
        return

    # Verifica se o comando é !rembg ou !removebg
    if message.content.lower() in ["!rembg", "!removebg"]:

        # Verifica se tem imagem anexada
        if not message.attachments:
            await message.reply(
                "❌ Anexe uma imagem junto com o comando!\n"
                "Exemplo: envie a imagem e escreva `!rembg` na mensagem."
            )
            return

        attachment = message.attachments[0]

        # Verifica se é uma imagem válida
        valid_types = ["image/png", "image/jpeg", "image/jpg", "image/webp"]
        if attachment.content_type not in valid_types:
            await message.reply("❌ Formato inválido! Use PNG, JPG ou WEBP.")
            return

        # Avisa que está processando
        processing_msg = await message.reply("⏳ Removendo fundo... aguarde!")

        try:
            # Baixa a imagem
            img_bytes = await attachment.read()

            # Remove o fundo com rembg
            input_img = Image.open(io.BytesIO(img_bytes)).convert("RGBA")
            output_img = remove(input_img)

            # Salva em memória como PNG
            output_buffer = io.BytesIO()
            output_img.save(output_buffer, format="PNG")
            output_buffer.seek(0)

            # Nome do arquivo de saída
            original_name = os.path.splitext(attachment.filename)[0]
            output_filename = f"{original_name}_sem_fundo.png"

            # Envia a imagem processada
            await message.reply(
                "✅ Pronto! Aqui está sua imagem sem fundo:",
                file=discord.File(fp=output_buffer, filename=output_filename),
            )

            # Apaga a mensagem de "processando"
            await processing_msg.delete()

        except Exception as e:
            await processing_msg.edit(content=f"❌ Erro ao processar a imagem: {str(e)}")


client.run(TOKEN)
