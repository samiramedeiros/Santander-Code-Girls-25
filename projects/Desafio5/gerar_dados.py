import json
import os
from faker import Faker
from datetime import datetime
import random

# Inicializa o Faker com localização para dados em Português do Brasil
fake = Faker('pt_BR')

# 1. Define o número de currículos (itens) a serem gerados
NUM_CURRICULOS = 5

def gerar_curriculo_fake():
    """Gera um dicionário de dados de currículo fake com todos os campos solicitados."""
    
    # --- Geração de Dados Base ---
    nome_completo = fake.name()
    primeiro_nome = nome_completo.split()[0]
    sobrenome = nome_completo.split()[-1]
    
    # Chave Primária (PK)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    id_curriculo = f"{primeiro_nome.lower()}-{sobrenome.lower()}-{timestamp}-{random.randint(100, 999)}"
    
    # --- Dados de Conteúdo (Solução do Desafio) ---
    profissoes = ["Desenvolvedor Python", "Cientista de Dados", "Arquiteto Cloud", "Engenheiro de DevOps", "Especialista em Segurança"]
    formacoes = ["Bacharel em Ciência da Computação", "Mestrado em Engenharia de Software", "Tecnólogo em Análise e Des. de Sistemas"]
    habilidades_base = ["Python", "AWS", "Docker", "Git", "SQL"]
    
    # Cria a estrutura que será salva no DynamoDB
    curriculo_data = {
        "IdCurriculo": id_curriculo,
        "NomeCompleto": nome_completo,
        "Localizacao": f"{fake.city()}, {fake.state_abbr()}",
        "Telefone": fake.phone_number(),
        "Email": fake.email(),
        "Profissao": random.choice(profissoes),
        "Formacao": random.choice(formacoes),
        "Experiencia": [
            {"Empresa": fake.company(), "Cargo": fake.job(), "Anos": random.randint(1, 5)},
            {"Empresa": fake.company(), "Cargo": fake.job(), "Anos": random.randint(1, 5)}
        ],
        "Habilidades": list(set(habilidades_base + [fake.word() for _ in range(random.randint(1, 3))])), # Adiciona 1 a 3 habilidades aleatórias
        "UltimaAtualizacao": datetime.now().isoformat()
    }
    
    return curriculo_data

def gerar_arquivo_json(num_itens):
    """Gera a lista de currículos e salva no arquivo JSON na pasta atual."""
    
    # Gera a lista de currículos
    curriculos = [gerar_curriculo_fake() for _ in range(num_itens)]
    
    # Salva no arquivo JSON (CORREÇÃO DE CAMINHO)
    nome_arquivo = "curriculos.json"
    
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(curriculos, f, indent=4, ensure_ascii=False)
        
        print(f"\n✅ {num_itens} currículos gerados com sucesso com campos completos!")
        print(f"Arquivo salvo como: {nome_arquivo}")
        
    except Exception as e:
        print(f"❌ Erro ao escrever o arquivo JSON: {e}")

if __name__ == "__main__":
    gerar_arquivo_json(NUM_CURRICULOS)