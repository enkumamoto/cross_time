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

````

🐛 Solução de Problemas

*   **Erro "Externally Managed Environment" no Linux:** Este erro ocorre ao tentar instalar pacotes globalmente. A solução é sempre usar um **ambiente virtual**, conforme descrito no passo 3 da instalação.
*   **Sem som no Linux:** Verifique se você instalou os pacotes `alsa-utils` e `beep` conforme a nota no passo 4.
*   **Porta 5000 já em uso:** Se outra aplicação estiver usando a porta 5000, você pode alterá-la no final do arquivo `cross_time.py`:
    ```python
    # Altere para a porta desejada, ex: 5001
    app.run(debug=True, host='0.0.0.0', port=5001)
    ```

📝 Personalização

*   **Tempo de Preparação:** Para alterar os 10 segundos iniciais, modifique o loop na função `timer_thread` dentro de `cross_time.py` (linha ~100).
*   **Sons e Notificações:** As funções `beep()` e `show_popup()` em `cross_time.py` podem ser customizadas para usar arquivos de som (`.mp3`, `.wav`) ou comandos de notificação diferentes.

🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para forkar o projeto, criar uma branch para sua feature e abrir um Pull Request.

1.  Fork o projeto.
2.  Crie sua branch de feature (`git checkout -b feature/AmazingFeature`).
3.  Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`).
4.  Push para a branch (`git push origin feature/AmazingFeature`).
5.  Abra um Pull Request.
````
