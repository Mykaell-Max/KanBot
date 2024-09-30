# Kanban Discord Bot

Um bot de Kanban para Discord que ajuda a gerenciar tarefas diretamente no servidor, criando, atualizando, visualizando e deletando tarefas organizadas por status.

## Funcionalidades

- **Adicionar tarefas**: Crie novas tarefas com nome, descrição e responsável.
- **Atualizar status**: Atualize o status de uma tarefa existente.
- **Excluir tarefas**: Exclua tarefas pelo nome.
- **Visualizar tarefas**: Veja todas as tarefas ou uma tarefa específica com status e responsáveis.
- **Suporte a MongoDB**: Todas as tarefas são armazenadas em um banco de dados MongoDB, permitindo persistência.

## Pré-requisitos

- **Python 3.8+**
- **MongoDB**: O projeto utiliza uma instância do MongoDB para armazenar as tarefas.
- **Discord Bot Token**: Um token de bot do Discord para autenticação.
- **Bibliotecas Python**: Instaladas com o `pip`.

## Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/Mykaell-Max/KanBot
cd KanBot
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # No Windows use: venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
Crie um arquivo .env na raiz do projeto e adicione suas chaves de configuração:
```bash
BOTTOKEN=seu-token-do-discord
MONGO=string-de-conexao-mongodb
```
### 5. Execute o bot
```bash
python bot.py
```

## Comandos disponíveis

Aqui estão os principais comandos que o bot oferece:

- k!add <nome> <descrição> <responsável> - Adiciona uma nova tarefa.
- k!update <nome> <status> - Atualiza o status de uma tarefa (Pending, In progress, Done).
- k!delete <nome> - Remove uma tarefa pelo nome.
- k!tasks - Exibe todas as tarefas, listando seus nomes e status.
- k!task <nome> - Exibe detalhes de uma tarefa específica.

## Exemplo de uso

```bash
k!add "Implement feature X" "Develop X for the project" "Max"
# Task added!

k!tasks
# ---------------------------------------------
# Task Name                     Status
# ---------------------------------------------
# Implement feature X           Pending
# ---------------------------------------------
```

## Estrutura do projeto

```bash
KanBot/
│
├── bot.py                  # Arquivo principal para iniciar o bot
├── commands.py             # Contém os comandos do bot
├── taskController.py       # Funções de interação com o MongoDB
├── embed.py                # Funções para criar mensagens embed
├── utils.py                # Funções utilitárias
├── mongo/
│   └── mongoConfig.py      # Configuração do MongoDB
├── .env                    # Variáveis de ambiente
└── README.md               # Documentação do projeto
```