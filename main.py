# Lista de Tarefas
import pandas as pd

# Dicionário para armazenar as tarefas
tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    horario = input("Digite o horário (HH:MM): ")
    tarefas.append({"Tarefa": tarefa, "Horário": horario})
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa adicionada ainda.")
    else:
        df = pd.DataFrame(tarefas)
        df = df.sort_values(by="Horário")  # Ordena as tarefas por horário
        print("\nLista de Tarefas:")
        print(df)

def exportar_para_excel():
    if not tarefas:
        print("Nenhuma tarefa para exportar.")
    else:
        df = pd.DataFrame(tarefas)
        df.to_excel("tarefas.xlsx", index=False)
        print("Tarefas exportadas para 'tarefas.xlsx'.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Exportar para Excel")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            exportar_para_excel()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
