# Use uma imagem base oficial do Python.
# python:3.9-slim é uma boa escolha por ser leve.
FROM python:3.12-slim

# Instala as dependências do sistema necessárias para sons e notificações no Linux.
# - alsa-utils: Fornece 'speaker-test' para emitir sons.
# - beep: Uma alternativa para emitir sons.
# - libnotify-bin: Fornece 'notify-send' para notificações de desktop.
# --no-install-recommends reduz o tamanho da imagem.
# Limpar o cache do apt no final para manter a imagem pequena.
RUN apt-get update && apt-get install -y --no-install-recommends \
    alsa-utils \
    beep \
    libnotify-bin \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container.
WORKDIR /app

# Copia o arquivo de dependências primeiro para aproveitar o cache do Docker.
# Se requirements.txt não mudar, esta camada não será reconstruída.
COPY requirements.txt .

# Instala as dependências do Python.
# --no-cache-dir reduz o tamanho da imagem.
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o diretório de trabalho.
COPY . .

# Expõe a porta em que a aplicação Flask será executada.
EXPOSE 5000

# Comando para executar a aplicação quando o container iniciar.
# O host 0.0.0.0 é necessário para que a aplicação seja acessível de fora do container.
CMD ["python", "cross_time.py"]

# NOTA SOBRE SOM E NOTIFICAÇÕES:
# Para que os sons e as notificações funcionem, você pode precisar
# compartilhar o hardware de som e o sistema D-Bus do host com o container ao executá-lo.
# Exemplo de comando de execução:
# docker run -it --rm -p 5000:5000 --device /dev/snd -v /run/user/$(id -u)/bus:/run/user/$(id -u)/bus cross-time