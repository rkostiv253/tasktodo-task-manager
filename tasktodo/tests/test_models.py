from django.contrib.auth import get_user_model
from django.test import TestCase

from tasktodo.models import Position, TaskType, Task, Worker
from datetime import datetime


class ModelTests(TestCase):

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="test")
        self.assertEqual(str(task_type), "test")

    def test_position_str(self):
        position = Position.objects.create(name="test")
        self.assertEqual(str(position), "test")


    def create_worker_with_position(self):
        username = "test"
        password = "test123"
        position = Position.objects.create(name="C+ developer")
        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            position=position,
        )
        self.assertEqual(worker.username, username)
        self.assertEqual(worker.position, position)
        self.assertTrue(worker.check_password(password))
        self.assertEqual(str(worker), "test")

    def create_task(self):
        name = "test"
        description = "123"
        deadline = (datetime.today())
        status = False
        priority = "ME"
        task_type = TaskType.objects.create(name="write test cases")
        position = Position.objects.create(name="C++ developer")
        worker1 = Worker.objects.create(
            username="test1", password="pass12352", position=position
        )
        worker2 = Worker.objects.create(
            username="test2", password="pass12352", position=position
        )
        task = Task.objects.create(
            name=name,
            description=description,
            deadline=deadline,
            status=status,
            priority=priority,
            task_type=task_type,
        )
        task.workers.set([worker1, worker2])
        self.assertEqual(task.name, name)
        self.assertEqual(task.description, description)
        self.assertEqual(task.deadline, deadline)
        self.assertEqual(task.status, status)
        self.assertEqual(task.priority, priority)
        self.assertEqual(task.task_type, task_type)
        self.assertEqual(set(task.workers.all()), {worker1, worker2})
        self.assertEqual(str(task), "test, 123")
