import sys
from storage import Storage
from task import Task


class TaskManager:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load_tasks()

    def add_task(self, title, description):
        task = Task(title=title, description=description)
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print("Tarefa adicionada com sucesso!")

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa cadastrada.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Concluída" if task.completed else "Pendente"
                print(f"{idx}. {task.title} - {status}")

    def list_incomplete_tasks(self):
        incomplete_tasks = [(idx, task) for idx, task in enumerate(self.tasks) if not task.completed]
        if not incomplete_tasks:
            print("Nenhuma tarefa pendente.")
        else:
            for real_idx, (idx, task) in enumerate(incomplete_tasks, start=1):
                print(f"{real_idx}. {task.title} (Índice real: {idx + 1}) - Pendente")

    def update_task(self, index, title, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = title
            self.tasks[index].description = description
            self.storage.save_tasks(self.tasks)
            print("Tarefa atualizada com sucesso!")
        else:
            print("Índice inválido!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.storage.save_tasks(self.tasks)
            print("Tarefa excluída com sucesso!")
        else:
            print("Índice inválido!")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.storage.save_tasks(self.tasks)
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido!")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar Tarefa")
            print("2. Listar Tarefas")
            print("3. Atualizar Tarefa")
            print("4. Excluir Tarefa")
            print("5. Marcar Tarefa como Concluída")
            print("6. Listar Tarefas Não Concluídas")
            print("7. Sair")
            print()

            choice = input("Escolha uma opção: ")

            if choice == "1":
                title = input("Título da Tarefa: ")
                description = input("Descrição da Tarefa: ")
                self.add_task(title, description)
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                index = int(input("Número da tarefa a atualizar: ")) - 1
                title = input("Novo título: ")
                description = input("Nova descrição: ")
                self.update_task(index, title, description)
            elif choice == "4":
                index = int(input("Número da tarefa a excluir: ")) - 1
                self.delete_task(index)
            elif choice == "5":
                index = int(input("Número da tarefa a marcar como concluída: ")) - 1
                self.mark_completed(index)
            elif choice == "6":
                self.list_incomplete_tasks()
            elif choice == "7":
                self.storage.save_tasks(self.tasks)
                print("Saindo...")
                sys.exit()
            else:
                print("Opção inválida!")
