# 🚀 Desafio 5 - Tarefas Automatizadas com Lambda Function e S3

## 🎯 Objetivo

Implementar uma automação com AWS Lambda, S3 e DynamoDB utilizando o LocalStack para simular o ambiente AWS localmente.
O objetivo é que, ao enviar um arquivo JSON para o bucket S3, a Lambda seja acionada automaticamente, processe os dados e os insira no DynamoDB.

## 🧩 Serviços Utilizados

- **AWS S3** – armazenamento dos arquivos JSON
- **AWS Lambda** – execução automática ao detectar novos arquivos
- **AWS DynamoDB** – banco de dados NoSQL para armazenar os dados processados
- **LocalStack** – simulação local da AWS
- **Docker Desktop** – execução do LocalStack
- **Python + Faker** – geração de dados fictícios

## 📂 Arquitetura Criada

<img width="803" height="322" alt="Diagrama" src="https://github.com/user-attachments/assets/80f0f817-7d29-4b91-aaea-3c1e4810a85d" />

## 🔗 Fluxo de Funcionamento

1. O script Python gera dados fictícios e salva em um arquivo curriculos.json.
2. Esse arquivo é enviado para o bucket S3.
3. O envio dispara a Lambda, que lê o arquivo do S3.
4. A Lambda insere os dados no DynamoDB.

# Etapa 1

### 1. Instale o Docker Desktop e Execute

Abra o Docker Desktop e clique no botão <img width="60" height="25" alt="docker restart" src="https://github.com/user-attachments/assets/42c369b7-c6db-43ed-a7f0-b9988f995de1" />

Aguarde até que no canto inferior esquerdo mostre a seguinte mensagem:

  <img width="238" height="26" alt="docker running" src="https://github.com/user-attachments/assets/1605f196-dc8d-4787-a459-72b5a4f47b03" />

### 2. Inicie o LocalStack: 

Execute o comando no seu terminal do VS Code:

```
  docker run -d --rm -p 4566:4566 -e SERVICES=s3,lambda,dynamodb,apigateway localstack/localstack
```

Para verificar se ele foi iniciado, copie e cole o comando abaixo no seu terminal do VS Code:
```
  docker ps
```
### 3. Instale Ferramentas CLI e Faker

```
pip install awscli awscli-local faker
```

### 4. Configure Credenciais AWS (Fictícias)

Execute os comandos a seguir no seu terminal:

```
aws configure set aws_access_key_id "test"
```
```
aws configure set aws_secret_access_key "test"
```
```
aws configure set region "us-east-1"
```
```
awslocal s3 ls
```

### 5. Gerar Dados

Salve o arquivo [**gerar_dados.py**](gerar_dados.py/) na sua pasta de execução do desafio.

Depois de salvar, execute o comando a seguir no seu terminal, para que o arquivo JSON com os dados gerados:

```
python gerar_dados.py
```
Pronto! Seu arquivo JSON com os dados foi gerado.

### 6. Criando o Bucket S3

Em um novo terminal no VS Code, execute o comando a seguir:

```
aws s3 mb s3://curriculos-bucket --endpoint-url=http://localhost:4566
```

Então, quando você verificar no site https://app.localstack.cloud/inst/default/resources/s3 deve se deparar com a informação a seguir:

<img width="1032" height="319" alt="bucket criado" src="https://github.com/user-attachments/assets/23ddb0f0-a62c-40d2-b579-7a7990640a35" />

### 7. Criando a Tabela DynamoDB

Salve o arquivo [**carregar_dynamo.py**](carregar_dynamo.py/) na sua pasta de execução do desafio.

Agora execute o comando abaixo no seu terminal. Ele instrui o AWS CLI a criar a tabela Curriculos no seu LocalStack, usando IdCurriculo como Chave de Partição (PK):

```
awslocal dynamodb create-table `
    --table-name Curriculos \
    --key-schema AttributeName=IdCurriculo,KeyType=HASH \
    --attribute-definitions AttributeName=IdCurriculo,AttributeType=S \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
```
Depois execute o comando para carregar os dados:

```
python carregar_dynamo.py
```

<img width="1029" height="388" alt="dynamodb criado" src="https://github.com/user-attachments/assets/0452dff9-8acd-46af-ab27-192923132d91" />

### 8. Provisione a Lambda e o S3

Nós acabamos de concluir a preparação e o provisionamento do DynamoDB.
Agora que a infraestrutura está estável, vamos focar na Lambda para a automação!

O objetivo é: Sempre que um arquivo JSON for enviado ao S3, a Lambda deve ser ativada para processar os dados e salvá-los no DynamoDB.

Vamos dividir em 3 passos:

- **Passo 1: Crie o Código da Lambda**

Salve o arquivo [**lambda_handler.py**](lambda_handler.py/) na sua pasta de execução do desafio.

A função Lambda precisa do código desse arquivo para receber o evento do S3, ler o arquivo JSON e inserir no DynamoDB.

- **Passo 2: Provisione a Função Lambda**

Vamos criar a função no LocalStack, empacotando o código acima. Execute o comando a seguir no Terminal do VS Code:

```
# Cria o arquivo ZIP que a Lambda vai usar
Compress-Archive -Path .\lambda_handler.py -DestinationPath .\lambda_function.zip
```

Verifique se o arquivo ```lambda_function.zip``` foi criado na sua pasta.

Agora execute o comando a seguir no Terminal do VS Code:

```
# Cria a função Lambda
aws lambda create-function `
    --function-name S3CurriculoProcessor `
    --runtime python3.9 `
    --handler lambda_handler.lambda_handler `
    --zip-file fileb://lambda_function.zip `
    --role arn:aws:iam::000000000000:role/irrelevant `
    --environment Variables="{DYNAMODB_ENDPOINT_URL=http://localstack:4566, AWS_ENDPOINT_URL=http://localstack:4566}" `
    --endpoint-url=http://localhost:4566
```

<img width="1027" height="404" alt="lambda handler criado" src="https://github.com/user-attachments/assets/9455a09e-c4ae-4fce-a51e-4502e98540ee" />


- **Passo 3: Crie o Gatilho (Trigger) S3**

Agora que o LocalStack tem o Bucket S3 (curriculos-bucket), o DynamoDB (Curriculos) e a Lambda (S3CurriculoProcessor), só falta dizer ao S3 para chamar a Lambda quando um arquivo for enviado.

Salve o arquivo [**s3_notification.json**](s3_notification.json/) na sua pasta de execução do desafio.

Execute este comando no seu terminal. Ele adiciona a política, permitindo que o S3 invoque a Lambda:

```
aws lambda add-permission `
    --function-name S3CurriculoProcessor `
    --statement-id "s3-invoke-lambda" `
    --action "lambda:InvokeFunction" `
    --principal "s3.amazonaws.com" `
    --source-arn "arn:aws:s3:::curriculos-bucket/*" `
    --endpoint-url=http://localhost:4566
  ```

Agora seu Bucket S3 terá permissão para invocar a Lambda.

Associe o gatilho:

```
aws s3api put-bucket-notification-configuration `
    --bucket curriculos-bucket `
    --notification-configuration file://s3_notification.json `
    --endpoint-url=http://localhost:4566
```

Teste enviando um arquivo:

```
aws s3 cp curriculos.json s3://curriculos-bucket/data/curriculos_upload.json --endpoint-url=http://localhost:4566
```

### Parabéns 🎉

A primeira etapa foi concluida com sucesso!

# ETAPA 2

Para completar o diagrama e permitir que o RH consulte os currículos no DynamoDB, precisamos criar uma API REST usando o API Gateway e uma segunda função Lambda de consulta.

O fluxo será: RH -> API Gateway -> Lambda de Consulta -> DynamoDB.

### **1. Crie o Código da Lambda de Consulta** ```consulta_handler.py```

Eu já deixei ele pronto. Salve o arquivo [**lambda_handler.py**](lambda_handler.py/) na sua pasta de execução do desafio.

Esta função Lambda receberá a requisição HTTP do API Gateway, consultará o DynamoDB e retornará a lista de currículos.

### **2. Provisione a Lambda de Consulta**

Agora, vamos empacotar e criar a segunda função Lambda, chamando-a de ```CurriculoConsultaFunction```

Execute o seguinte comando no Terminal do VS Code: 

Empacotar o novo código:

```
Compress-Archive -Path .\consulta_handler.py -DestinationPath .\consulta_lambda.zip
```

```
# Criar a função Lambda de Consulta
aws lambda create-function `
    --function-name CurriculoConsultaFunction `
    --runtime python3.9 `
    --handler consulta_handler.lambda_handler `
    --zip-file fileb://consulta_lambda.zip `
    --role arn:aws:iam::000000000000:role/irrelevant `
    --environment Variables="{DYNAMODB_ENDPOINT_URL=http://localstack:4566}" `
    --endpoint-url=http://localhost:4566
```

### **3. Crie e Ligue o API Gateway**

Para conectar o mundo HTTP à sua Lambda de consulta, execute a sequência de comandos abaixo no Terminal do seu VS Code:

### **a) Criar o API Gateway:**

```
API_ID=$(aws apigateway create-rest-api --name "CurriculoAPI" --endpoint-url=http://localhost:4566 | jq -r '.id')
echo "API ID criada: $API_ID"
```

(Se você não tiver ```jq``` instalado, você precisará copiar o valor de ```id``` da resposta JSON e usá-lo na variável ```$API_ID```.)


### **b) Obter o ID do Recurso Raiz (```/```):**

```
ROOT_RESOURCE_ID=$(aws apigateway get-resources --rest-api-id $API_ID --endpoint-url=http://localhost:4566 | jq -r '.items[] | select(.path == "/") | .id')
```

### **c) Criar o Recurso de Consulta (```/curriculos```):**

```
RESOURCE_ID=$(aws apigateway create-resource --rest-api-id $API_ID --parent-id $ROOT_RESOURCE_ID --path-part "curriculos" --endpoint-url=http://localhost:4566 | jq -r '.id')
```

### d) Criar o Método GET no Recurso:

```
aws apigateway put-method --rest-api-id $API_ID --resource-id $RESOURCE_ID --http-method GET --authorization-type NONE --endpoint-url=http://localhost:4566
```

### **e) Ligar o Método GET à Função Lambda:**

```
LAMBDA_ARN="arn:aws:lambda:us-east-1:000000000000:function:CurriculoConsultaFunction"

aws apigateway put-integration --rest-api-id $API_ID --resource-id $RESOURCE_ID --http-method GET --type AWS_PROXY --integration-http-method POST --uri "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/$LAMBDA_ARN/invocations" --endpoint-url=http://localhost:4566
```

### **f) Adicionar Permissão para o API Gateway Chamar a Lambda:**

```
aws lambda add-permission --function-name CurriculoConsultaFunction --statement-id "ApiGatewayInvoke" --action "lambda:InvokeFunction" --principal "apigateway.amazonaws.com" --source-arn "arn:aws:execute-api:us-east-1:000000000000:$API_ID/*/*/*" --endpoint-url=http://localhost:4566
```

### **g) Fazer o Deploy da API:**

```
aws apigateway create-deployment --rest-api-id $API_ID --stage-name dev --endpoint-url=http://localhost:4566
```

### 4. **Teste Final: Consulte a API**

Se todos os comandos acima foram bem-sucedidos, você pode testar a consulta.

A URL base no LocalStack é sempre ```http://localhost:4566/restapis/[API_ID]/[STAGE_NAME]/_user_request_/[RESOURCE_PATH]```

O link de consulta será:

```
http://localhost:4566/restapis/$API_ID/dev/_user_request_/curriculos
```

Cole esse link no seu navegador (substituindo ```$API_ID``` pelo valor que você obteve no passo 3a) ou use o ```curl``` no terminal:

```
curl http://localhost:4566/restapis/$API_ID/dev/_user_request_/curriculos
```

### Parabéns 🎉

A segunda etapa foi concluida com sucesso!


## ✅ Conclusão

Este desafio foi um grande aprendizado sobre como construir uma automação robusta e eficiente do zero.

Minha maior lição foi sobre a arquitetura serverless (S3, Lambda, DynamoDB):

- Consegui desacoplar o recebimento dos currículos do processamento, tornando o sistema altamente escalável e resiliente a picos de tráfego.

- A solução é custo-efetiva porque só pagamos quando o código da Lambda é executado, eliminando a manutenção de servidores ociosos.

- Para o RH, a experiência é de tempo real: o API Gateway e o DynamoDB garantem que a consulta de currículos seja ultrarrápida, otimizando todo o processo de recrutamento.

No fim, demonstrei que essa arquitetura é a chave para construir sistemas modernos que são, ao mesmo tempo, poderosos e economicamente inteligentes.

