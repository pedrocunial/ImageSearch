# Buscador de Imagens
Pedro Cunial -- Insper 2018

## Resumo

Desenvolvido para a disciplina de Visão Computacional do Insper (2018), o projeto baseia-se em um modelo de rede neural [(MobileNetV2)](https://arxiv.org/abs/1801.04381), para encontrar imagens próximas a uma dada palavra-chave.

As palavras chaves possíveis são descritas pelos [rótulos da ImageNet](https://gist.githubusercontent.com/yrevar/942d3a0ac09ec9e5eb3a/raw/c2c91c8e767d04621020c30ed31192724b863041/imagenet1000_clsid_to_human.txt)


## Uso

### Dependências

As dependências do projeto estão descritas no `requirements.txt`. Apesar do projeto ter um `Pipfile`, existe uma incompatibilidade entre as versões mais recentes.

Para instalar as dependências use: `pip install -r requirements.txt`

### Rodando

O programa é basicamente dividido em duas partes, a indexação da base de dados e a busca de um rótulo na base

Para fazer a indexação use:

`python main.py --build-index` ou `python main.py --train`

O programa espera uma pasta chamada `data` na raíz do projeto contendo diversas pastas cada uma com imagens a serem rotuladas. Adicionalmente, pode-se passar o _path_ relativo da pasta utilizando o argumento `--dir`

`python main.py --build-index --dir <path para diretório utilizado>`

Para buscar por uma palavra-chave, basta utilizar o argumento `--term` ou `--search`

`python main --term <palavra-chave>`

## Resultados

Ao executar uma busca, o programa retorna as cinco imagens mais próximas do termo escolhido, bem como o as suas probabilidades.

Por exemplo, para o termo `banana`, a imagem de melhor probabilidade retornada foi (com 99% de certeza):

![banana](aux/banana5.jpg)


No entanto, nem todos os termos existentes no ImageNet estão representados no _dataset_, por exemplo, ao buscar pelo termo `scuba diver`, a imagem de maior probabilidade foi (com 2,15% de certeza):

![scubadiver](aux/deku4.jpeg)
