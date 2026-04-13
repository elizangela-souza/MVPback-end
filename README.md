# API Cooperativa de Reciclagem

>Este projeto é o resultado do MVP da sprint Desenvolvimento Full Stack Básico e buscou atender uma necessidade básica de uma cooperativa de reciclagem, que seria o armazenamento e consulta das informações referentes ao resultado do processo de triagem. 

Esse processo envolve algumas instâncias, sendo estas o cooperado que reliza o processo de triagem e o material reciclável que é separado, preensado e armazenado. Dessa forma, foi desenvolvido métodos para:

- Incluir, consultar, listar e excluir os registros dos cooperados;
- Atualizar apenas o nome e telefone do registro dos cooperados considerando que os demais atributos são únicos para o banco de dados, como a mátricula do cooperado, ou que não fazem sentido lógico serem alterados no decorrer do tempo, como a data de nascimento.
- Incluir, consultar, listar e excluir os registros dos materiais recicláveis;
- Atualizar apenar o valor_kg do registro dos materiais recicláveis considerando que os demais atributos são únicos para o banco de dados, como o código do material, ou devem ser alterados por uma regra de negócio, como o atributo quantidade_kg.
- Atualizar o estoque de materiais recicláveis, atributo quantidade_kg, após cada triagem realizada;
- Incluir, listar os registros das triagens;
- Não há atualização na tabela de registro de triagem tendo em vista que ela representa informações históricas do processo do trabalho dos cooperados.

## Tecnologias utilizadas
As principais ferramentas utilizadas no desenvolvimento:
- Python 
- Flask
- SQLAlchemy

## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

