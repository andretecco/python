# Anotações sobre o Curso
Ambiente
- ipython
- virtualenv(venv)

Links:
- [PyFormat](https://pyformat.info/)

Palavra Dunder.
- Palavra que substitui underline. ex:
`__version__ ` - Ao invés de dizer "underline, underline version, underline, underline" diria apenas Dunder version.

# Protocolos e Tipos de Dados
> Classe, categoria, tipo

Através para do tipo de dado o Python sabe o que você quer.
Exemplo: Número, letra e etc.

# Tipos de Dados
>Primários - Scalar types (representa um único valor)

dir(int) - mostra as opções que podem ser utilizadas com um tipo de dado int
métodos que não começam com _(underline), bit_count são metodos públicos.

numero = 65
numero.bit_count() - essa função mostra quantos bits foram utilizados para armazenar "numero", que no caso é o número inteiro 65

métodos que começam com dois underlines (nome do underline é dunder), são chamados de protocolos
Exemplo: dunder add (__add__)

>Compostos e Tuplas
- list, range