# API Cooperativa de Reciclagem

>Este projeto é o módulo API(back-end) do MVP da Sprint Desenvolvimento Back-end Avançado. Ele foi desenvolvido para atender às necessidades de armazenamento e consulta de informações de uma cooperativa de reciclagem.


## Funcionalidades
Esse projeto envolve algumas instâncias, sendo estas o cooperado que realiza o processo de triagem e o material reciclável que é separado, prensado e armazenado. O cliente que compra esse material que foi triado pela cooperativa para realizar o processo de reciclagem. Dessa forma, foi desenvolvido métodos para:

### Cooperado 
- Incluir, consultar, listar e excluir os registros dos cooperados.
- Atualizar apenas nome e telefone do registro dos cooperados, considerando que os demais atributos são únicos para o banco de dados, como a matrícula do cooperado, ou que não fazem sentido lógico serem alterados no decorrer do tempo, como a data de nascimento.

### Cliente
- Incluir, consultar, listar e excluir os registros dos clientes.
- Incluir informações do endereço do cliente no banco de dados a partir de consulta do cep do cliente na API externa [ViaCep](https://viacep.com.br/).
- Atualizar nome, cep, e-mail e telefone do registro dos clientes, considerando que o cnpj é um registro imutável. Ao atualizar o cep, a API externa viaCEP é acionada novamente e as demais informações de endereço são atualizadas.

### Triagem
- Incluir, consultar e listar os registros de triagem.
- Não há atualização na tabela de registro de triagem tendo em vista que elas representam informações históricas do trabalho dos cooperados.

### Venda
- Incluir, consultar e listar os registros de venda.
- Incluir o valor da venda a partir das informações registradas (quantidade_kg e categoria de material reciclável). O cálculo é feito consultando o valor por quilograma da categoria na tabela de Materiais Recicláveis.
- Não há atualização na tabela de registro de venda tendo em vista que elas representam informações históricas das vendas realizadas.

### Material reciclável
- Incluir na tabela de Material Reciclável um novo registro de material quando uma categoria nova for registrada na triagem.
- Atualizar o estoque de materiais recicláveis, atributo quantidade_kg, após cada triagem e venda realizadas.

## Tecnologias utilizadas
As principais ferramentas utilizadas no desenvolvimento:
- Python 
- Flask
- SQLAlchemy

## Como executar com Dockerfile

### 1. Utilizar o comando no terminal `docker build -t api-backend .`
Para construir a imagem a partir do Dockerfile.

Caso esteja utilizando Windows, deve primeiro abrir o aplicativo [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/?uuid=BBEA0E54-C959-4598-A02E-B324AE057A35#system-requirements) no seu computador e ter instalado o WSL2 ou uma máquina virtual interna.

### 2. Utilizar o comando no terminal `docker run -d -p 5000:5000 api-backend`
Para criar e inicializar o container a partir da imagem api-backend já construída.

### 3. Acessar a aplicação pelo link [http://localhost:5000/](http://localhost:5000/) no navegador

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

