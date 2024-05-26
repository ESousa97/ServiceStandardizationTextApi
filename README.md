# Service Standardization Text Api

Este projeto consiste em uma API desenvolvida em Flask que fornece um serviço de normalização de texto. A API permite que os usuários enviem textos através de uma requisição HTTP POST e recebem esses textos normalizados como resposta. A normalização de texto inclui a remoção de acentos e a conversão de todos os caracteres para minúsculas.

## Detalhes da Funcionalidade
### Rota `/normalize`:

- **Método:** `POST`
- **Entrada:** Um JSON contendo uma lista de textos sob a chave `texts`.
- **Processo:** Cada texto na lista é normalizado removendo os acentos e convertendo todos os caracteres para minúsculas.
- **Saída:** Um JSON contendo a lista de textos normalizados.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- Python 3.12
- pip (gerenciador de pacotes do Python)
- Node.js e npm (gerenciador de pacotes do Node.js)

## Instalação

### Backend (Flask)

**1. Clone o repositório:**

```bash

git clone <URL-do-repositório>
cd <nome-do-diretório>

```

**2. Crie um ambiente virtual:**

```bash

python3 -m venv env
source env/bin/activate  # Para Linux/Mac
.\env\Scripts\activate   # Para Windows

```

**3. Instale as dependências do Python:**

```bash

pip install -r requirements.txt

```
### Frontend (Next.js)

**1. Instale as dependências do `Node.js`:**

```bash

npm install

```
## Execução

### Backend

**1. Inicie o servidor Flask:**

```bash

python api/app.py

```
O servidor estará rodando em `http://127.0.0.1:5005`.

## Estrutura dos Arquivos

- **api/app.py**: Código principal da API Flask.
- **package.json**: Arquivo de configuração do Node.js com scripts e dependências.
- **vercel.json**: Arquivo de configuração para implantação no Vercel.
- **requirements.txt**: Lista de dependências do Python.

## Endpoints da API

### Processamento
Para cada texto na lista:

- Os caracteres são normalizados utilizando `unicodedata.normalize('NFKD', text)`.
- Os caracteres acentuados são removidos através de `.encode('ASCII', 'ignore').decode('utf-8')`.
- O texto é convertido para minúsculas com `.lower()`.

### Normalize
- **URL:** `/normalize`

- **Método:** `POST`

- **Descrição:** Normaliza uma lista de textos, removendo acentos e convertendo para minúsculas.

- **Exemplo de Requisição:**

```bash

{
  "texts": ["Olá Mundo", "API de Teste"]
}

```
- **Exemplo de Resposta:**

```bash

[
  "ola mundo",
  "api de teste"
]

```

## Implantação no Vercel

**1. Configure o Vercel CLI:**

```bash

npm install -g vercel
vercel login

```
**2. Implante o projeto:**

```bash

vercel

```

## Dependências

- **Flask:** Framework web para Python.
- **Flask-CORS:** Extensão para permitir CORS.
- **Werkzeug:** Biblioteca WSGI para Python.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

##

Este serviço pode ser integrado em várias aplicações onde a uniformidade dos dados textuais é crucial, como em motores de busca, sistemas de análise de texto, e qualquer aplicação que lide com entrada de texto do usuário.