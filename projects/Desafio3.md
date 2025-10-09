# 🚀 Desafio 3 - Criando sua Primeira Stack com CloudFormation

### 📚 O que é AWS CloudFormation?

AWS CloudFormation é um serviço que permite criar e gerenciar recursos da AWS usando arquivos de modelo. Com o CloudFormation, você pode definir sua infraestrutura como código (IaC), facilitando a automação e a replicação de ambientes.

### 🧩 O que é uma Stack

Uma Stack é um conjunto de recursos AWS (como EC2, S3, RDS, etc.) criados e gerenciados juntos a partir de um template CloudFormation (um arquivo .yaml ou .json que descreve a infraestrutura).

### 🚀 Como criar sua primeira Stack na AWS (usando Upload a template file)
**Pré-requisitos**

1. Ter uma conta AWS e estar logada no AWS Management Console.

2. Ter o arquivo do template salvo no seu computador (ex: meu-template.yaml).

Se ainda não tiver o template, posso te mostrar um exemplo básico logo abaixo.

### 🔗 Passo a passo

### Passo 1 - **Acesse o CloudFormation**

Vá em:
- https://console.aws.amazon.com/cloudformation

- Clique em **"Create stack"** (Criar pilha).

### Passo 2 - **Escolha o método**

- Em **"Prepare template"**, selecione:
    <p>✅ “Choose an existing template”</p>

- Logo abaixo, selecione:
    <p>✅ “Upload a template file”</p>
    
> Vou deixar abaixo uma opção para você copiar e colar
```AWSTemplateFormatVersion: '2010-09-09'
Description: Cria um bucket S3 com versionamento e bloqueio público habilitado

Parameters:
  BucketNamePrefix:
    Type: String
    Description: Prefixo para o nome do bucket (deve ser único globalmente)
    Default: meu-bucket-teste

Resources:
  MeuBucketS3:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "${BucketNamePrefix}-${AWS::AccountId}"
      VersioningConfiguration:
        Status: Enabled
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true

Outputs:
  NomeDoBucket:
    Description: Nome do bucket criado
    Value: !Ref MeuBucketS3
```

- Clique em “Choose file” e selecione o seu arquivo .yaml ou .json.

  <img width="1030" height="468" alt="Passo - Bucket-s3" src="https://github.com/user-attachments/assets/1083ddf2-baf3-4348-9b02-da35778eb453" />

- Depois clique em **“Next”**.


### Passo 3 - **Defina os detalhes da Stack**

- Em **Stack name**, coloque o nome da sua stack, por exemplo:
minha-primeira-stack

  <img width="1048" height="449" alt="passo - detalhes" src="https://github.com/user-attachments/assets/4eaa6fde-a290-4324-94b8-f8cb6e358f96" />


- Clique em **“Next”**.

### Passo 4 - **Configurações opcionais**

- Aqui você pode configurar:

    - Tags (identificação)

    - Permissões (Role do IAM)

    - Opções avançadas (notificações, rollback, etc.)

- Se for apenas um teste, pode deixar tudo padrão.

- Clique em **“Next”**.

### Passo 5 - **Revisar e criar**

- Revise todas as informações.

- Se o template cria recursos que geram custos (como EC2), a AWS mostrará um aviso.

- Marque a caixa de confirmação e clique em **“Submit”** ao final da pagina.

### Passo 6 - **Acompanhar o progresso**

- Você será levado à tela de **“Stack details”**.

- Acompanhe o status na aba **Events** até aparecer (pode levar alguns minutos):

> CREATE_COMPLETE


### Pronto 🎉 Sua primeira Stack está criada!
