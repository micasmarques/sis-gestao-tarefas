import unittest
import sys
import os

# Adicionar o diretório src ao caminho de busca de módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task_manager import TaskManager  # Importar diretamente do arquivo task_manager.py

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()
        self.manager.tasks = []

    def test_add_task(self):
        self.manager.add_task("Tarefa 1", "Descrição da tarefa 1")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].title, "Tarefa 1")
        self.assertEqual(self.manager.tasks[0].description, "Descrição da tarefa 1")

    def test_list_tasks(self):
        self.manager.add_task("Tarefa 1", "Descrição da tarefa 1")
        self.manager.add_task("Tarefa 2", "Descrição da tarefa 2")
        self.assertEqual(len(self.manager.tasks), 2)

    def test_list_incomplete_tasks(self):
        self.manager.add_task("Task 1", "Description 1")
        self.manager.add_task("Task 2", "Description 2")
        self.manager.mark_completed(0)
        incomplete_tasks = [task for task in self.manager.tasks if not task.completed]
        self.assertEqual(len(incomplete_tasks), 1)

    def test_update_task(self):
        self.manager.add_task("Tarefa 1", "Descrição da tarefa 1")
        self.manager.update_task(0, "Tarefa Atualizada", "Nova descrição")
        self.assertEqual(self.manager.tasks[0].title, "Tarefa Atualizada")
        self.assertEqual(self.manager.tasks[0].description, "Nova descrição")

    def test_delete_task(self):
        self.manager.add_task("Tarefa 1", "Descrição da tarefa 1")
        self.manager.delete_task(0)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_mark_completed(self):
        self.manager.add_task("Tarefa 1", "Descrição da tarefa 1")
        self.manager.mark_completed(0)
        self.assertTrue(self.manager.tasks[0].completed)
        self.assertIsNotNone(self.manager.tasks[0].completed_at)

if __name__ == "__main__":
    unittest.main()
