# 🚀 Desafio 2 - Explorando Workflows Automatizados com AWS Step Functions

### 🎯 Objetivo

Implementar um sistema para ligar e desligar instâncias utilizando AWS Step Functions para orquestrar diferentes serviços em um fluxo controlado e visual, permitindo tomadas de decisão baseadas em dados em tempo real.

### 🧩 Serviços Utilizados

- **AWS Step Functions**: Orquestração do workflow
- **AWS Lambda**: Execução de funções serverless
- **Amazon SQS**: Filas para aprovação humana
- **Amazon SNS**: Notificações de resultados
- **AWS IAM**: Gerenciamento de permissões

### 📂 Arquitetura Criada

<img width="344" height="402" alt="Diagrama desafio2" src="https://github.com/user-attachments/assets/0598f9f9-64c4-48af-8fa1-1343664838d3" />


A arquitetura foi desenvolvida seguindo princípios de microserviços:
1. Componentes desacoplados
2. Responsabilidades bem definidas
3. Escalabilidade independente
4. Alta resiliência

Estrutura dos componentes:

- Funções Lambda para processamento
- Filas SQS para aprovações assíncronas
- Tópicos SNS para notificações
- Estados de decisão para controle de fluxo

## 🔗 Fluxo de Funcionamento

1. Início do Workflow
   - Trigger automático ou manual
   - Inicialização dos parâmetros
   - Verificação de Status

2. Lambda consulta status da instância
   - Processamento da instância
   - Análise e Recomendação

3. Lambda gera recomendação (Stop/Start)
   - Baseado em algoritmos predefinidos
   - Aprovação Humana

4. Envio para fila SQS
   - Aguarda decisão do usuário
   - Execução da Operação

5. Choice state determina ação
   - Lambda executa Stop ou Start
   - Notificação

6. SNS envia resultado
   - Status da instância

### ✅ Conclusão

O projeto demonstrou a eficácia do AWS Step Functions na orquestração de microserviços, oferecendo:

- Visualização clara do fluxo de trabalho
- Integração seamless entre serviços AWS
- Escalabilidade e confiabilidade
- Recursos para Aprofundamento
- Documentação oficial AWS Step Functions
- AWS Well-Architected Framework
- Cursos especializados em microserviços
- Workshops práticos da AWS
