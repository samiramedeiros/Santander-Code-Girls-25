import json
import boto3
import os

# Configurações para LocalStack
# Usamos variáveis de ambiente para o endpoint_url
DYNAMODB_ENDPOINT_URL = os.environ.get('DYNAMODB_ENDPOINT_URL', 'http://localstack:4566')
REGION_NAME = 'us-east-1' 
TABLE_NAME = 'Curriculos'

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=DYNAMODB_ENDPOINT_URL,
    region_name=REGION_NAME
)
s3_client = boto3.client(
    's3',
    endpoint_url=DYNAMODB_ENDPOINT_URL, # S3 usa o mesmo endpoint no LocalStack
    region_name=REGION_NAME
)
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # 1. Obter informações do evento S3
        record = event['Records'][0]
        bucket_name = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        print(f"Novo objeto detectado: {key} no bucket {bucket_name}")

        # 2. Baixar e ler o arquivo JSON do S3
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        file_content = response['Body'].read().decode('utf-8')
        
        # O arquivo JSON deve ser uma lista de currículos
        curriculos_list = json.loads(file_content)

        # 3. Inserir os dados no DynamoDB
        count = 0
        with table.batch_writer() as batch:
            for item in curriculos_list:
                # O DynamoDB espera um dicionário.
                batch.put_item(Item=item)
                count += 1

        print(f"✅ Sucesso: {count} itens inseridos na tabela '{TABLE_NAME}' após processar o arquivo {key}.")

        return {
            'statusCode': 200,
            'body': f'Processados {count} itens do arquivo {key}'
        }

    except Exception as e:
        print(f"❌ Erro ao processar o arquivo S3: {e}")
        raise e