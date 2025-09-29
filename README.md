⏰ Cross Time - Cronômetro Inteligente
Um cronômetro inteligente desenvolvido em Python com Flask para controle de tempo com rounds, descansos e sinais sonoros.

🚀 Funcionalidades
⏱️ Contagem Progressiva: Tempo dos rounds conta progressivamente

🔄 Múltiplos Rounds: Configure quantos rounds desejar

☕ Tempo de Descanso: Intervalos entre rounds com contagem regressiva

🔊 Sinais Sonoros: Alertas audíveis em intervalos configuráveis

🎯 Contagem Regressiva Inicial: 10 segundos de preparação antes do primeiro round

📱 Interface Web: Frontend responsivo e intuitivo

⏹️ Controle em Tempo Real: Iniciar, parar e monitorar o progresso

🛠️ Tecnologias Utilizadas
Backend: Python 3.7+, Flask

Frontend: HTML5, CSS3, JavaScript

Multiplataforma: Compatível com Windows, Linux e macOS

Sinais Sonoros: Suporte nativo para cada sistema operacional

📦 Instalação
Pré-requisitos
Python 3.7 ou superior

pip (gerenciador de pacotes do Python)

Passos para Instalação
Clone o repositório:

bash
git clone <url-do-repositorio>
cd cross-time
Crie um ambiente virtual (recomendado):

bash
python3 -m venv venv
source venv/bin/activate # Linux/Mac

# ou

venv\Scripts\activate # Windows
Instale as dependências:

bash
pip install Flask==2.3.3
Instale dependências do sistema (Linux):

bash

# Para sinais sonoros

sudo apt update
sudo apt install alsa-utils

# Para notificações desktop

sudo apt install libnotify-bin
🎮 Como Usar
Configuração Básica
Tempo Total: Duração total em minutos (ex: 15 minutos)

Rounds: Número de divisões do tempo total (ex: 3 rounds)

Descanso: Tempo de pausa entre rounds em segundos (ex: 30 segundos)

Intervalo: Sinal sonoro a cada X minutos (0 para desativar)

Exemplo de Configuração
Tempo Total: 15 minutos

Rounds: 3

Descanso: 30 segundos

Intervalo: 5 minutos

Resultado: 3 rounds de 5 minutos cada, com 30 segundos de descanso entre eles, e sinal sonoro a cada 5 minutos.

Fluxo de Execução
Preparação: 10 segundos de contagem regressiva

Round 1: Contagem progressiva de 0 até 5:00

Descanso: 30 segundos de contagem regressiva

Round 2: Inicia imediatamente após o descanso

Repetição: Continua até completar todos os rounds

🖥️ Executando a Aplicação
Inicie o servidor:

bash
python cross_time.py
Acesse no navegador:

text
http://localhost:5000
Configure e inicie o timer:

Preencha os campos desejados

Clique em "Iniciar Timer"

Acompanhe o progresso em tempo real

🎯 Casos de Uso
🏋️‍♂️ Treinos e Exercícios
Timer de HIIT: Rounds intensos com descansos controlados

Treino em Circuito: Múltiplos exercícios com tempo definido

Alongamento: Tempos progressivos para cada posição

📚 Estudos e Produtividade
Técnica Pomodoro: 25 minutos de foco, 5 minutos de descanso

Sessões de Estudo: Múltiplas sessões com pausas programadas

Revisões: Tempos dedicados para diferentes matérias

💼 Reuniões e Apresentações
Timeboxing: Controle de tempo para cada tópico

Apresentações: Divisão do tempo entre seções

Brainstorming: Rounds cronometrados para ideias

⌨️ Comandos Rápidos
Enter: Iniciar timer (quando o formulário está em foco)

Botão "Iniciar Timer": Inicia o cronômetro

Botão "Parar Timer": Interrompe a execução atual

Botão "Limpar": Reseta o formulário

🔧 Estrutura do Projeto
text
cross-time/
│
├── cross_time.py # Backend Flask
├── requirements.txt # Dependências Python
├── README.md # Este arquivo
└── templates/
└── index.html # Frontend da aplicação
🐛 Solução de Problemas
Erro "Externally Managed Environment"
bash

# Use ambiente virtual

python3 -m venv venv
source venv/bin/activate
Sem som no Linux
bash

# Instale dependências de áudio

sudo apt install alsa-utils beep
Porta já em uso
bash

# Altere a porta no cross_time.py

app.run(debug=True, host='0.0.0.0', port=5001)
📝 Personalização
Modificando o Tempo de Preparação
No arquivo cross_time.py, linha ~50:

python

# Alterar de 10 para o valor desejado

for i in range(10, 0, -1):
Customizando Sinais Sonoros
Modifique a função beep() no cross_time.py para usar sons personalizados.

🤝 Contribuindo
Fork o projeto

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

🆕 Versões Futuras
Configurações salvas automaticamente

Múltiplos perfis de timer

Histórico de sessões

Modo escuro/claro

Notificações personalizadas

Export de relatórios
