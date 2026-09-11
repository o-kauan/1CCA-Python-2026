from model import model_lead
import control

def add_lead ():
    name = input("Nome: ")
    email = input("E-mail: ")
    stage = input("Etapa de vendas: ")

# 1 validar dados
# 1,5 estruturar em dicionários
# 2 adicionar na base de dados

    print(model_lead(name, email, stage))

# 3 enviar os dados para o leads.json
# 4 o control.py irá auxiliar a enviar os dados para o

    control.create_lead(model_lead(name, email, stage))

def list_leads():
    leads = control.read_lead()
    print(leads)

def main ():
    while True:
        print("\nMini CRM de Leads")
        print("[1] adicionar lead")
        print("[2] lista de leads")
        print("[0] Sair do sistema")

        opt = input("Escolha uma opcção: ")
        if opt == "1":
            add_lead()
            print("Lead adicionado")

        elif opt == "2":
            print("Lista de Leads")
            list_leads()

        elif opt == "0":
            print("Saindo...")
            return
        else:
            print("Aí não né fi")


if __name__ == "__main__": # só vai executar se o arquivo for o app,
    main()                 # se for importado para outro, essa parte não funciona lá

