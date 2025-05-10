import whisper

# Carrega o modelo base (pode ser: tiny, base, small, medium, large)
modelo = whisper.load_model("base")

# Transcreve o áudio do arquivo
resposta = modelo.transcribe("Gravando2.m4a")

# Imprime apenas o texto transcrito
print(resposta["text"])

