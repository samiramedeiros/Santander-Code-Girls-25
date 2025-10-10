# 🚀 Desafio 4 - Implementar uma infraestrutura automatizada com AWS CloudFormation

### 📚 O que é AWS CloudFormation?

O AWS CloudFormation é a ferramenta nativa da AWS para Infraestrutura como Código (IaC), o que permite automatizar o provisionamento e o gerenciamento de seus recursos, garantindo consistência, repetibilidade e reduzindo erros manuais.

### 💡 Conceitos Principais

Antes de começar a codificar, é crucial entender a terminologia do CloudFormation:

- **Template (Modelo)**: É um arquivo de texto formatado em YAML ou JSON que descreve todos os recursos da AWS que você deseja criar (por exemplo, instâncias EC2, VPCs, Bancos de Dados RDS, Load Balancers, etc.) e suas configurações.

- **Resource (Recurso)**: É o componente da AWS que você está provisionando (ex: AWS::EC2::Instance, AWS::S3::Bucket). O Template lista todos eles.

- **Stack (Pilha)**: É o conjunto de recursos criados pelo CloudFormation a partir de um Template. Quando você executa um Template, o CloudFormation cria uma Stack e gerencia todos os recursos dentro dela como uma única unidade.

- **Change Set (Conjunto de Alterações)**: É uma visualização das alterações que o CloudFormation fará nos seus recursos antes de aplicá-las. Isso é vital para entender o impacto de uma atualização no seu Template.

### 💳 Cenário: 

E-mails automáticos de cobrança de cartão de crédito.

### 🎯 Objetivo

No dia 10 de cada mês, o sistema deve enviar automaticamente um e-mail de cobrança aos clientes informando o valor e a data de vencimento da fatura.

### ☁️ Arquitetura AWS para Fluxo de Cobrança

| Componente | Serviço AWS | Função |
| :--- | :--- | :--- |
| **Agendador mensal** | Amazon EventBridge | Dispara o fluxo no dia 10 de cada mês. |
| **Orquestração** | AWS Step Functions | Coordena as etapas do workflow de cobrança. |
| **Lógica de envio** | AWS Lambda | Envia os e-mails de cobrança. |
| **Serviço de e-mail** | Amazon SES | Serviço de envio real das mensagens. |
| **Infraestrutura como Código** | AWS CloudFormation | Automatiza a criação e gerenciamento de todos os recursos da infraestrutura. |

### 🔗 Passo a passo

### Passo 1 - **Acesse o CloudFormation**

Vá em:
- https://console.aws.amazon.com/cloudformation

- Clique em **"Create stack"** (Criar pilha).

### Passo 2 - **Escolha o método**

- Em **"Preparar modelo"**, selecione:
    <p>✅ “Escolher um modelo existente”</p>

- Logo abaixo, selecione:
    <p>✅ “Fazer upload de um arquivo de modelo”</p>

    [**Clique Aqui e Copie este Template**](template-banco.yaml/)

- Clique em "Escolher Arquivo" e selecione o seu arquivo .yaml ou .json.

    <img width="1011" height="280" alt="2" src="https://github.com/user-attachments/assets/fd9cc269-3fb1-47f6-9074-b3730a358c01" />

- Depois clique em **“Próximo”**.

### Passo 3 - **Defina os detalhes da Stack**

- Em **Fornecer um nome de pilha**, coloque o nome da sua pilha, por exemplo:
CobrancaCartaodeCredito

  <img width="1050" height="449" alt="3" src="https://github.com/user-attachments/assets/cca9fca5-188f-4406-a2e2-a38a70fa3ac6" />


- Clique em **“Próximo”**.

### Passo 4 - **Configurações opcionais**

- Aqui você pode configurar:

    - Tags (identificação)

    - Permissões (Role do IAM)

    - Opções avançadas (notificações, rollback, etc.)

- Se for apenas um teste, pode deixar tudo padrão.

- Clique em **“Próximo”**.

### Passo 5 - **Revisar e criar**

- Revise todas as informações.

- Se o template cria recursos que geram custos (como EC2), a AWS mostrará um aviso.

- Marque a caixa de confirmação e clique em **“Submit”** ao final da pagina.

### Passo 6 - **Acompanhar o progresso**

- Você será levado à tela de **“Informações da pilha”**.

- Acompanhe o status na aba **Eventos** até aparecer (pode levar alguns minutos):

> CREATE_COMPLETE
  <img width="418" height="450" alt="5" src="https://github.com/user-attachments/assets/a0bdd2fb-93a3-4961-addc-feb8ff3790ca" />

## 🎉 Pronto! Sua Stack está criada!


## 🧪 Testes e Considerações

### ✔️ Verificações antes de rodar:

- O e-mail especificado como Source (remetente) deve estar verificado no Amazon SES (principalmente se estiver em sandbox).
- Você pode usar SSM Parameter Store ou o parâmetro EmailOrigem para definir o e-mail remetente.
- Para sair do sandbox do SES, é necessário abrir um ticket com a AWS.

### 🧠 Possíveis Extensões

- Integrar com DynamoDB para buscar valores e e-mails dos clientes dinamicamente.
- Usar SNS ou SQS para monitoramento do fluxo.
- Adicionar alertas com CloudWatch Alarms se a execução da Step Function falhar.
- Utilizar Templates de e-mail personalizados com HTML no SES.

### ✅ Conclusão

  Este desafio demonstrou como a AWS, combinando serviços como Lambda, Step Functions e SES, permite automatizar processos críticos como envio de cobranças mensais. Com o uso do AWS CloudFormation, foi possível provisionar toda a infraestrutura de forma automatizada, garantindo escalabilidade, padronização e facilidade de manutenção. A abordagem adotada pode ser reutilizada em diversos cenários de notificações recorrentes, reforçando os benefícios da Infraestrutura como Código (IaC).
