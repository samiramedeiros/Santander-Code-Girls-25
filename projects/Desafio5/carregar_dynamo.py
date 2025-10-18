import boto3
import json
from botocore.exceptions import ClientError

# Configurações para o LocalStack
DYNAMODB_ENDPOINT_URL = 'http://localhost:4566'
REGION_NAME = 'us-east-1' # Região padrão para LocalStack
TABLE_NAME = 'Curriculos'
JSON_FILE = 'curriculos.json'

# Inicializa o cliente DynamoDB para LocalStack
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=DYNAMODB_ENDPOINT_URL,
    region_name=REGION_NAME
)

try:
    # Tenta acessar a tabela Curriculos (que já confirmamos que existe)
    table = dynamodb.Table(TABLE_NAME)
    
    # Abrir o arquivo JSON com os currículos gerados
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = 0
    
    print(f"Iniciando o carregamento de {len(data)} currículos na tabela '{TABLE_NAME}'...")

    # Itera sobre a lista de currículos e insere cada um como um item
    for item in data:
        table.put_item(
           Item=item
        )
        count += 1

    print("-" * 30)
    print(f"✅ Sucesso! {count} itens foram inseridos na tabela '{TABLE_NAME}'.")

except FileNotFoundError:
    print(f"❌ ERRO: Arquivo '{JSON_FILE}' não encontrado. Certifique-se de que o 'gerar_dados.py' foi executado.")
except ClientError as e:
    print(f"❌ ERRO do DynamoDB/LocalStack: {e.response['Error']['Message']}")
except Exception as e:
    print(f"❌ Ocorreu um erro inesperado: {e}")