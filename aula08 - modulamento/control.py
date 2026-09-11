from idlelib.iomenu import encoding
from pathlib import Path #manipular pastas
import json #dicionário != joson

DATA_DIR = Path(__file__).resolve().parent / "data"
# print(DATA_DIR) # = C:\Users\labsfiap\PycharmProjects\1CCA-Python-2026\aula08 - modulamento\data\leads.json
DATA_DIR.mkdir(exist_ok = True) # cria essa pasta, (só se ela não existir)
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREATE / READ / UPDATE / DELETE

# --- READ ---

def read_lead():
    if not DB_PATH.exists():
        return [] # 0 leads
    try:
        return json.loads(DB_PATH.read_text(encoding = "utf-8")) # vai tentar pegar para dados do python
    except json.JSONDecodeError:                       # utf-8 é o padrão de codificação nosso portugueso e acentos e ç
        return [] #  bruh

print(read_lead())

# --- CREATE ---

def create_lead (lead_dict):
    leads = read_lead()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent = 2, encoding = "utf-8")) # reescreve em formato de json (e não ascii), indet é o tab
