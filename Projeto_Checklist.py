import json
from pathlib import Path
checklist_tarefa = []
import time

# Recebe o caminho do JSON 
caminho = Path(__file__).parent / "tarefas_checklist.json"

# Copia na lista os valores presentes no JSON
with open(caminho,'r',encoding='utf-8') as f:
    checklist_tarefa = json.load(f)

def menu():
    print("*"*40)
    print("Tarefas - Checklist")
    print("a) Adicionar Tarefa")
    print("b) Listar Tarefa")
    print("c) Marcar como Concluída")
    print("d) Remover Tarefa")
    print("e) Finalizar Programa")
def adicionar(): # Função com objetivo de adicionar tarefas
    dicionario = {}
    
    dicionario["Tarefa"] = input("Digite o nome da tarefa: ")
    dicionario["Situacao"] = False
    
    if not dicionario["Tarefa"]:
        print("Por favor, coloque uma tarefa!")
        return
    else:
        for n in checklist_tarefa:
            if n["Tarefa"] == dicionario["Tarefa"]:
                print("Não pode colocar tarefa repetida")
                return    
        checklist_tarefa.append(dicionario)
        print("Tarefa adicionada!")
        with open(caminho,'w',encoding="utf-8") as f:
            json.dump(checklist_tarefa,f,indent=2)
def listar(): # Função com o objetivo de listar as tarefas
    if not checklist_tarefa:
        print("A lista de tarefas está vazia")
    else:
        print("LISTA DE TAREFAS ")
        for i in checklist_tarefa:
            if i['Situacao'] is False:
                print(f"Tarefa: {i['Tarefa']}") 
                print(f"Situação: [ ] - Não Concluído") 
            else: 
                print(f"Tarefa: {i['Tarefa']}") 
                print(f"Situação: [X] - Tarefa Concluída")
        time.sleep(3)
        print("*"*40)
def marcar_concluida():
    if not checklist_tarefa:
        print("A lista de tarefas está vazia")
        return
    j = 1
    for i in checklist_tarefa:
        if i['Situacao'] is False:
            print(f"{j}) Tarefa {j}")
            print(f"Tarefa: {i['Tarefa']}")
            print(f"Situação: [ ] - Não Concluído")
        else:
            print(f"{j}) Tarefa {j}")
            print(f"Tarefa: {i['Tarefa']}")
            print(f"Situação: [X] - Tarefa Concluída")
        j += 1
    time.sleep(3)    

    try:
        indice = int(input("Digite o indice correspondente a atividade que deseja marcar como concluida: "))
        if indice < 1 or indice > len(checklist_tarefa):
            print("Digite um índice válido")
            return
        checklist_tarefa[indice-1]['Situacao']=True
        with open(caminho,'w',encoding="utf-8") as f:
            json.dump(checklist_tarefa,f,indent=2)


    except ValueError:
        print("Digite um número")

def remover():
    if not checklist_tarefa:
        print("A lista de tarefas está vazia")
        return

    j = 1
    for i in checklist_tarefa:
        if i['Situacao'] is False:
            print(f"{j}) Tarefa {j}")
            print(f"Tarefa: {i['Tarefa']}")
            print(f"Situação: [ ] - Não Concluído")
        else:
            print(f"{j}) Tarefa {j}")
            print(f"Tarefa: {i['Tarefa']}")
            print(f"Situação: [X] - Tarefa Concluída")
        j += 1

    time.sleep(3)

    try:
        x = int(input("Digite o indice da tarefa que deseja remover: "))

        if x < 1 or x > len(checklist_tarefa):
            print("Digite um índice válido")
            return

        del checklist_tarefa[x-1]

        with open(caminho,'w',encoding="utf-8") as f:
            json.dump(checklist_tarefa,f,indent=2)

        print("Tarefa removida com sucesso!")

    except ValueError:
        print("Digite um número válido")


def opcoes():
    opcao = input("Selecione a letra correspondente ao seu desejo: ").upper()
    print("*"*40)

    if opcao == "A":
        return adicionar()
    elif opcao == "B":
        return listar()
    elif opcao == "C":
        return marcar_concluida()
    elif opcao == "D":
        return remover()
    elif opcao == "E":
        return "E"
while True:
    menu()
    if opcoes() == "E":
        with open(caminho,'w',encoding="utf-8") as f: # Guarda as informações novas no JSON
            json.dump(checklist_tarefa,f,indent=2)
        break






