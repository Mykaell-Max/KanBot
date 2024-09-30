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