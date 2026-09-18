from pathlib import Path # manipular pastas
import json, csv # dicionário != json

DATA_DIR = Path(__file__).resolve().parent / "data"
# print(DATA_DIR) # = C:\Users\labsfiap\PycharmProjects\1CCA-Python-2026\aula08 - modulamento\data\leads.json
DATA_DIR.mkdir(exist_ok = True) # cria essa pasta, (só se ela não existir)
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREATE / READ / UPDATE / DELETE

# --- READ ---
def read_leads():
    if not DB_PATH.exists():
        return [] # 0 leads
    try:
        return json.loads(DB_PATH.read_text(encoding = "utf-8")) # vai tentar pegar para dados do python
    except json.JSONDecodeError:                       # utf-8 é o padrão de codificação nosso portugueso e acentos e ç
        return [] #  bruh

print(read_leads())

# --- CREATE ---
def create_lead (lead_dict):
    leads = read_leads() #não pode carregar a base toda toda hora
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent = 2), encoding = "utf-8") # reescreve em formato de json (e não ascii), indet é o tab

# FUNÇÃO QUE BUSCA LEADS DE ACORDO COM A QUERY E RETORNA UMA LISTA COM RESULTADOS
def read_leads_search(query):
    leads = read_leads() # lista de leads / lista de dicts / array of dicts
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]}".lower()
        if query.lower() in txt_lead:
            results.append((i, lead))
    return results

def export_csv():
    """ Exporta os leads para csv e RETORNA o caminho ao arquivo csv"""
    path_csv = DATA_DIR / "Leads.csv"
    leads = read_leads()

    try:
        with path_csv.open ("w", newline = "", encoding = "utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()
            for row_dict in leads:
                writer.writerow(row_dict)
        return path_csv
    except PermissionError:
        return None

