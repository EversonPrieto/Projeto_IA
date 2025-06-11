# Contador de Pessoas com YOLOv8 e DeepSort
Este repositório contém um projeto Python para contagem de pessoas em tempo real, utilizando `uv` como gerenciador de pacotes e executor de comandos.

O sistema detecta pessoas em um vídeo, as rastreia com ID e conta quantas cruzam uma linha virtual, registrando entradas e saídas.

## Pré-requisitos

Certifique-se de ter o uv instalado em seu sistema. Se não tiver, você pode instalá-lo seguindo as instruções na documentação oficial do uv.

## Instalação
Clone este repositório:
```
git clone <url_do_seu_repositorio>
cd <PROJETO_IA>
```

Crie o ambiente virtual e instale as dependências usando `uv sync`:
```
# Cria e ativa o ambiente virtual automaticamente e instala os pacotes
uv sync
```
Este comando lerá o `pyproject.toml` e instalará exatamente as dependências listadas.

Se precisar "Consertar" o Ambiente
Para garantir que o seu ambiente sempre saiba onde está seu código, você pode "instalar" seu projeto em modo editável.
```
uv pip install -e .
```

## Utilização
## 1. Configuração do Script
Antes de rodar, abra o arquivo main.py e ajuste as seguintes constantes:
```
VIDEO_PATH: O caminho para o seu arquivo de vídeo.

LINE_Y: A posição vertical da linha de contagem.
```

## 2. Rodar o Programa Principal
Para executar o contador de pessoas, utilize o comando `uv run`:
```
uv run main.py
```
Este comando executa o script main.py usando o interpretador Python do ambiente virtual gerenciado pelo `uv`. Pressione q na janela do vídeo para sair.

Estrutura do Projeto
A estrutura recomendada para este projeto é a seguinte:
```
Projeto_IA/
├── src/
│   ├── contador_pessoas.egg-info/
│   └── meu_modulo/
│       ├── __init__.py
│       ├── contador_logic.py
│       └── __pycache__/
│
├── tests/
│   ├── __init__.py
│   ├── test_contador_logic.py
│   └── __pycache__/
│
├── .venv/
├── .pytest_cache/
│
├── main.py 
├── istockphoto-1152080347-640_adpp_is.mp4
├── yolov8l.pt
├── yolov8n.pt
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```
main.py: O ponto de entrada principal, contendo toda a lógica de detecção (YOLOv8), rastreamento (DeepSort) e contagem.

pyproject.toml: O coração da configuração do projeto, usado pelo uv para gerenciar dependências e o ambiente.

## 3. Rodar o Programa de Testes

1. test_entrada_sucesso: Confirma que se uma pessoa cruza a linha de cima para baixo, o sistema conta uma entrada.

2. test_saida_sucesso: Confirma que se uma pessoa cruza a linha de baixo para cima, o sistema conta uma saída.

3. test_sem_cruzamento: Confirma que se uma pessoa se move mas não cruza a linha, o sistema não conta nada. 

4. test_primeira_aparicao: Confirma que quando uma pessoa aparece pela primeira vez, o sistema a registra, mas não conta nem entrada nem saída ainda.

No seu terminal, navegue até a pasta raiz do seu projeto (a pasta que contém o pyproject.toml) e execute:
```
uv run pytest
```