# Contador de Pessoas com YOLOv8 e DeepSort
Este repositório contém um projeto Python para contagem de pessoas em tempo real, utilizando `uv` como gerenciador de pacotes e executor de comandos.

O sistema detecta pessoas em um vídeo, as rastreia com ID e conta quantas cruzam uma linha virtual, registrando entradas e saídas.

## Pré-requisitos

Certifique-se de ter o uv instalado em seu sistema. Se não tiver, você pode instalá-lo seguindo as instruções na documentação oficial do uv.

Instalação
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

## Utilização
1. Configuração do Script
Antes de rodar, abra o arquivo main.py e ajuste as seguintes constantes:
```
VIDEO_PATH: O caminho para o seu arquivo de vídeo.

LINE_Y: A posição vertical da linha de contagem.
```

2. Rodar o Programa Principal
Para executar o contador de pessoas, utilize o comando `uv run`:
```
uv run main.py
```
Este comando executa o script main.py usando o interpretador Python do ambiente virtual gerenciado pelo `uv`. Pressione q na janela do vídeo para sair.

Estrutura do Projeto
A estrutura recomendada para este projeto é a seguinte:
```
src/meu_modulo
├──__init__.py          # torna 'meu_modulo' um pacote Python
├── main.py             # O script principal que realiza a contagem
├── video_exemplo.mp4   # Coloque aqui o vídeo que deseja processar
pyproject.toml          # Define o projeto e suas dependências
README.md               # Este arquivo
uv.lock                 # trava as versões exatas de todos os pacotes para garantir que as instalações sejam sempre idênticas e reproduzíveis.

```
main.py: O ponto de entrada principal, contendo toda a lógica de detecção (YOLOv8), rastreamento (DeepSort) e contagem.

pyproject.toml: O coração da configuração do projeto, usado pelo uv para gerenciar dependências e o ambiente.
