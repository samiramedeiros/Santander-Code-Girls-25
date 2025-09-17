# 🚀 Desafio 1 DIO - Santander Code Girls

Neste desafio, criamos uma **arquitetura no Draw.io** para consolidar o conhecimento em **gerenciamento de instâncias EC2 na AWS**.

### 🎯 Objetivo
Projetar uma arquitetura **simples e funcional** utilizando alguns dos principais serviços da AWS.

### 🧩 Serviços Utilizados

#### 🟦 **Amazon S3**
- Serviço de **armazenamento de objetos** (arquivos, imagens, vídeos, backups etc).  
- Permite configurar **gatilhos** para outros serviços quando novos arquivos são enviados.  
- Muito usado para **armazenar dados de forma segura e escalável**.

#### 🟨 **AWS Lambda**
- Serviço **serverless** que executa funções sob demanda.  
- É acionado por **eventos** (ex: um arquivo enviado para o S3).  
- Excelente para tarefas rápidas como:  
  - **Validação de arquivos**  
  - **Transformação de dados**  
  - **Extração de metadados**

#### 🟥 **Amazon EC2**
- Serviço de **máquinas virtuais (IaaS)** na nuvem.  
- Permite rodar:  
  - **Aplicações web**  
  - **APIs**  
  - **Bancos de dados**  
- É um dos pilares da AWS, oferecendo **flexibilidade e escalabilidade**.

#### 🟫 **Amazon EBS**
- Serviço de **armazenamento em bloco** acoplado ao EC2.  
- Funciona como um **HD/SSD persistente**, garantindo que os dados sejam preservados mesmo que a instância seja desligada.  
- Ideal para bancos de dados ou aplicações que precisam de **armazenamento confiável**.

### 📂 Arquitetura Criada

<img width="747" height="393" alt="Desafio 1" src="https://github.com/user-attachments/assets/02f941fc-323b-4a58-8780-8c56684845a7" />

### 🔗 Fluxo de Funcionamento

1. 👤 O **usuário** envia um **arquivo** para o **Amazon S3**.  
2. 🤖 O **AWS Lambda** é acionado automaticamente para processar o arquivo (Podendo ser: validação, transformação ou extração de informações)  
3. 💻 O resultado é enviado para a **instância EC2**, que pode rodar uma aplicação para consumir esse dado.  
4. 📦 O **Amazon EBS** fornece armazenamento persistente para o EC2.  
5. 🌍 O **EC2** disponibiliza os dados ou resultados para o **usuário final** quando necessário.  

### ✅ Conclusão

Este desafio ajudou a **entender a integração entre diferentes serviços da AWS**.  
A arquitetura final mostra como unir:  

- **Armazenamento escalável** → Amazon S3  
- **Processamento sob demanda** → AWS Lambda  
- **Servidores virtuais flexíveis** → Amazon EC2  
- **Armazenamento persistente** → Amazon EBS  

⚡ Essa combinação cria uma base sólida para aplicações modernas na nuvem.
