from model import model_lead
import control

def add_lead ():
    name = input("Nome: ")
    email = input("E-mail: ")
    stage = input("Etapa de vendas: ")

# 1 validar dados
# 1,5 estruturar em dicionários
# 2 adicionar na base de dados
# 2.5 print(model_lead(name, email, stage))
# 3 enviar os dados para o leads.json
# 4 o control.py irá auxiliar a enviar os dados para o

    control.create_lead(model_lead(name, email, stage))

def list_leads():
    leads = control.read_leads()
    print(f"ID | {"Nome":<10} | {"E-mail"}")
    print("-" * 50)
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta Vazia :c")
        return

    # chamar o control e passar nossa query (busca)
    # o control irá verificar se existe a query no leads.json
    # e irá retornar os resultados da busca
    found_leads = control.read_leads_search(query)

    print(f"ID | {"Nome":<10} | {"E-mail"}")
    print("-" * 50)
    for i, lead in found_leads:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar os leads")
    else:
        print(f"Leads {path_csv}")

def main ():
    while True:
        print("\nMini CRM de Leads")
        print("[1] adicionar lead")
        print("[2] lista de leads")
        print("[3] Buscar (nome/email)")
        print("[4] Exportar para CSV")
        print("[0] Sair do sistema")

        opt = input("Escolha uma opcção: ")
        if opt == "1":
            add_lead()
            print("Lead adicionado")

        elif opt == "2":
            print("Lista de Leads")
            list_leads()

        elif opt == "3":
            print("Buscar (nome ou email)")
            search_leads()

        elif opt == "4":
            print("Expotando para CSV...")
            export_leads()

        elif opt == "0":
            print("Saindo...")
            return
        else:
            print("Aí não né fi")


if __name__ == "__main__": # só vai executar se o arquivo for o app,
    main()                 # se for importado para outro, essa parte não funciona lá

