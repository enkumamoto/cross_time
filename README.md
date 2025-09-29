<div align="center">

  <img src="https://raw.githubusercontent.com/Eiji-S/cross-time/main/assets/logo.png" alt="Cross Time Logo" width="150">

# Cross Time - Cronômetro Inteligente

**Um cronômetro web inteligente para gerenciamento de tempo, ideal para treinos, estudos e produtividade.**

  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python">
    <img alt="Flask" src="https://img.shields.io/badge/Flask-2.3.3-black?style=for-the-badge&logo=flask">
    <img alt="License" src="https://img.shields.io/github/license/Eiji-S/cross-time?style=for-the-badge">
  </p>

</div>

---

**Cross Time** é uma aplicação web construída com Python e Flask que oferece um cronômetro altamente configurável. Crie sessões de trabalho, estudo ou treino com múltiplos rounds, pausas para descanso e alertas sonoros, tudo controlado por uma interface simples e intuitiva.

## 📋 Índice

- [✨ Funcionalidades](#-funcionalidades)
- [🛠️ Tecnologias](#-tecnologias)
- [🚀 Começando](#-começando)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
- [🎮 Como Usar](#-como-usar)
- [🔧 Estrutura do Projeto](#-estrutura-do-projeto)
- [🤝 Contribuindo](#-contribuindo)
- [📄 Licença](#-licença)

## ✨ Funcionalidades

- **🔄 Múltiplos Rounds:** Divida o tempo total em quantos rounds precisar.
- **☕ Descanso Configurável:** Defina pausas com contagem regressiva entre os rounds.
- **🔊 Alertas Sonoros:** Receba alertas em intervalos de tempo e nas transições de fase.
- **🎯 Contagem Inicial:** Tenha 10 segundos de preparação antes do início da sessão.
- **📊 Progresso em Tempo Real:** Monitore o tempo e o progresso do round atual e da sessão total.
- **📱 Interface Web Intuitiva:** Frontend limpo, responsivo e fácil de usar.
- **🖥️ Multiplataforma:** Compatível com Windows, macOS e Linux, incluindo suporte a notificações e sons nativos.

## 🛠️ Tecnologias

- **Backend:** Python 3.7+, Flask
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)

## 🚀 Começando

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

- **Python 3.7 ou superior**
- **Git**

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/Eiji-S/cross-time.git
    cd cross-time
    ```

2.  **Crie e ative um ambiente virtual** (altamente recomendado):

    ```bash
    # Linux / macOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências** a partir do arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

    > **Nota para usuários Linux:** Para a melhor experiência com sons e notificações, instale as seguintes dependências do sistema:
    >
    > ```bash
    > sudo apt update && sudo apt install alsa-utils libnotify-bin
    > ```

4.  **Execute a aplicação:**

    ```bash
    python cross_time.py
    ```

5.  **Acesse no navegador:**
    Abra seu navegador e visite **http://localhost:5000**.

## 🎮 Como Usar

1.  **Configure sua sessão** no formulário principal:

    - `Tempo Total (minutos)`: Duração completa da atividade.
    - `Número de Rounds`: Em quantas partes o tempo será dividido.
    - `Tempo de Descanso (segundos)`: Pausa entre cada round.
    - `Intervalo para Sinal Sonoro (minutos)`: Emite um som a cada `X` minutos (use `0` para desativar).

2.  **Inicie o cronômetro** clicando em `▶ Iniciar Timer` ou pressionando a tecla `Enter`.

3.  **Acompanhe o progresso** em tempo real nos painéis de informação.

4.  **Pare a sessão** a qualquer momento clicando em `⏹ Parar Timer`.

## Estrutura do Projeto

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
