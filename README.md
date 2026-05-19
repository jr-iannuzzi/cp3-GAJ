# 🚀 HOW TO: CP3 - API REST com Docker e MySQL

## 📌 Descrição

Este projeto consiste na criação de uma API REST desenvolvida em Python utilizando Flask, com persistência de dados em banco MySQL, ambos executando em containers Docker.

A aplicação implementa operações de CRUD (Create, Read, Update e Delete) sobre uma entidade de produtos.

---

## 🧱 Tecnologias Utilizadas

- Python 3
- Flask
- MySQL 8
- Docker
- Azure Virtual Machine

---

## 📂 Estrutura do Projeto

```
cp3/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
├── database/
│   └── init.sql
├── scripts/
│   ├── 01-network.sh
│   ├── 02-volume.sh
│   ├── 03-mysql.sh
│   ├── 04-api.sh
│   ├── 05-all.sh
├── README.md
```

---

## ⚙️ Execução do Projeto

### 1. Dar permissão aos scripts

```bash
chmod +x scripts/*.sh
```

### 2. Executar o projeto completo

```bash
cd scripts
./05-all.sh
```

---

## 🐳 Containers Criados

| Container    | Descrição            |
|--------------|----------------------|
| `mysql-cp3`  | Banco de dados MySQL |
| `api-cp3`    | API Flask            |

---

## 🗄️ Banco de Dados

O banco é criado automaticamente através do script:

```
database/init.sql
```

Tabela criada:

```sql
produtos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  preco DECIMAL(10,2)
)
```

---

## 🌐 Endpoints da API

### 🔹 Criar produto

```
POST /produtos
```

### 🔹 Listar produtos

```
GET /produtos
```

### 🔹 Atualizar produto

```
PUT /produtos/{id}
```

### 🔹 Deletar produto

```
DELETE /produtos/{id}
```

---

## 🧪 Exemplo de Requisição

```bash
curl -X POST http://localhost:5000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome":"Mouse","preco":100}'
```

---

## 🔗 Comunicação entre Containers

Os containers utilizam uma rede Docker personalizada:

```
dimdim-network
```

---

## 💾 Persistência de Dados

Foi utilizado um volume Docker:

```
mysql-volume
```

Garantindo que os dados não sejam perdidos ao reiniciar o container.

---

## 🔐 Segurança

A aplicação Flask é executada dentro do container utilizando um usuário não-root, garantindo maior segurança e evitando privilégios desnecessários.

---

## 📌 Observações

- O banco de dados é inicializado automaticamente via script SQL
- A aplicação utiliza conexão entre containers via nome do serviço
- O ambiente é totalmente containerizado, garantindo portabilidade

---

## 👨‍💻 Autores

|--------------|----------------------|
| `ARTHUR CORREIA DELILA`  | RM563806 |
| `JOSÉ RICARDO `    | RM564112            |
| `GABRIEL HENRIQUE `    | RM563732            |

Projeto desenvolvido para a disciplina de Cloud Computing / DevOps.
