# Sistema de Gestão de Tarefas

Este projeto é um sistema de gestão de tarefas simples, que permite adicionar, listar, atualizar, excluir e marcar tarefas como concluídas. O sistema utiliza Python e é gerenciado com Docker.

## Pré-requisitos

Certifique-se de ter o seguinte instalado em sua máquina:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Estrutura do Projeto

- sis-gestao-tarefas/
    - src/
      - init.py
      - task_manager.py
      - storage.py
      - task.py
    - tests/
      - init.py
      - test_task_manager.py
    - Dockerfile
    - docker-compose.yml
    - requirements.txt 
    - README.md

## Configuração do Ambiente

### 1. Configuração do Docker

Este projeto utiliza Docker para isolar o ambiente de execução. A configuração do Docker está definida no arquivo `docker-compose.yml`.

### 2. Build e Execução

Para construir e iniciar o contêiner, use o comando:

```bash
docker-compose up
```
Este comando irá construir a imagem do Docker.

Por questões que no projeto estou usando o CLI, esse comando mostra um erro de EOF, e por isso para executar o aplicativo, é preciso executar o comando abaixo.

### 3. Executar o Aplicativo
Para executar o aplicativo diretamente no contêiner, use:

```bash
docker-compose run --rm back python3 /app/src/main.py
```

- `docker-compose run`: Executa um comando em um contêiner de serviço.
- `--rm`: Remove o contêiner após a execução.
- `back`: Nome do serviço definido no docker-compose.yml.
- `python3 /app/src/main.py`: Comando para rodar o script Python principal.

Esse comando é útil para testar o aplicativo ou executar comandos específicos sem iniciar o contêiner em modo contínuo.

### 4. Rodar os Testes
Para rodar os testes unitários, siga estes passos:
1. Certifique-se de que o contêiner está parado.
2. Execute os testes usando o comando:
   ```bash
   docker-compose run --rm back python3 -m unittest discover -s tests
   ```
   - `docker-compose run`: Executa um comando em um contêiner de serviço.
   - `--rm`: Remove o contêiner após a execução.
   - `back`: Nome do serviço definido no docker-compose.yml.
   - `python3 -m unittest discover -s tests`: Comando para descobrir e executar os testes no diretório tests.

### Estrutura dos Arquivos
- `src/task_manager.py`: Contém a lógica principal do gerenciamento de tarefas.
- `src/storage.py`: Responsável pela persistência dos dados em JSON.
- `src/task.py`: Define a estrutura de uma tarefa.
- `tests/test_task_manager.py`: Contém os testes unitários para o TaskManager.

### Notas
- Se você encontrar problemas de importação ao executar os testes, verifique se a estrutura do projeto está correta e se o diretório src está incluído no PYTHONPATH.
- Os arquivos de configuração do Docker e do Docker Compose garantem que o ambiente de execução seja consistente entre diferentes máquinas e ambientes.
