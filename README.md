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
