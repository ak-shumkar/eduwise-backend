from rest_framework.test import APITestCase, APIClient
from users.models import User, AGENT, STUDENT
from utils.logging.logger import logger


class BaseTestCase(APITestCase):
    @staticmethod
    def ok(msg=''):
        logger.log(1, msg + ": PASSED")

    def setUp(self) -> None:

        self.agent_json = {'username': 'recruiter', 'password': 'admin123', 'role': AGENT}
        self.agent = User.objects.create_user(**self.agent_json)
        self.assertTrue(self.agent.is_agent)

        self.student_json = {'username': 'employee', 'password': 'admin123', 'role': STUDENT}
        self.student = User.objects.create_user(**self.student_json)
        self.assertTrue(self.student.is_student)

        self.client = APIClient()
        self.ok('Test case setup')

    def test(self):
        pass
