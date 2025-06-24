from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from tasktodo.forms import (
    TaskTypeSearchForm,
    PositionSearchForm,
    WorkerSearchForm,
    TaskSearchForm
)


class SearchTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='test',
            password='pass12352',
        )
        self.client.login(username='test', password='pass12352')

    def test_search_task_type(self):
        response = self.client.get(reverse("tasktodo:task-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["search_form"], TaskTypeSearchForm)

    def test_search_position(self):
        response = self.client.get(reverse("tasktodo:position-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["search_form"], PositionSearchForm)

    def test_search_worker(self):
        response = self.client.get(reverse("tasktodo:worker-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["search_form"], WorkerSearchForm)

    def test_search_task(self):
        response = self.client.get(reverse("tasktodo:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["search_form"], TaskSearchForm)
