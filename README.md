# API Cooperativa de Reciclagem

>Este projeto é módulo API(back-end) do MVP da sprint Desenvolvimento Back-end Avançado, que visou atender a necessidade de armazenamento e consulta das informações de uma cooperativa de reciclagem.


Esse processo envolve algumas instâncias, sendo estas o cooperado que reliza o processo de triagem e o material reciclável que é separado, preensado e armazenado. O cliente que compra esse material que foi triado pela cooperativa para realizar o processo de reciclagem. Dessa forma, foi desenvolvido métodos para:

- Incluir, consultar, listar e excluir os registros dos cooperados e clientes.
- Atualizar apenas o nome e telefone do registro dos cooperados, considerando que os demais atributos são únicos para o banco de dados, como a mátricula do cooperado, ou que não fazem sentido lógico serem alterados no decorrer do tempo, como a data de nascimento.
- Incluir informações do endereço do cliente no banco de dados a partir de consulta do cep do cliente na API externa [ViaCep](https://viacep.com.br/).
- Atualizar o nome, cep, email e telefone do registro dos clientes, considerando que o cnpj é único do banco de dados. Ao atualizar o cep, a API externa viaCEP é acionada novamente e as demais informações de endereço são atualizadas.
- Incluir, consultar e listar os registros de triagem e de venda.
- Incluir o valor da venda após a inclusão das informações da venda, quantidade_kg e categoria de material reciclável.
- Incluir na tabela de Material Reciclável um material quando um material de categoria nova é triado.
- Atualizar o estoque de materiais recicláveis, atributo quantidade_kg, após cada triagem e venda realizadas.
- Não há atualização na tabela de registro de triagem e da tabela de venda tendo em vista que elas representam informações históricas do trabalho dos cooperados e das vendas realizadas.

## Tecnologias utilizadas
As principais ferramentas utilizadas no desenvolvimento:
- Python 
- Flask
- SQLAlchemy

## Como executar com Dockerfile

### 1. Utilizar o comando no terminal `docker build -t api-backend .`
Para construir a imagem.

### 2. Utilizar o comando no terminal `docker run -p 3000:80 api-backend`
Para rodar o container.

### 3. Acessar o link []() no navegador.

## Como executar sem Dockerfile

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

