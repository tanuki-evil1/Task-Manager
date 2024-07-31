from task_manager.tasks.forms import TaskCreateForm
from .testcase import TaskTestCase


class TaskFormTest(TaskTestCase):
    def test_valid_form(self) -> None:
        task_data = self.test_task['create']['valid'].copy()
        form = TaskCreateForm(data=task_data)

        self.assertTrue(form.is_valid())

    def test_invalid_form(self) -> None:
        task_data = self.test_task['create']['missing_fields'].copy()
        form = TaskCreateForm(data=task_data)

        self.assertFalse(form.is_valid())
