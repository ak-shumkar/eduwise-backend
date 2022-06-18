from rest_framework.test import APITestCase, APIClient
from eduwise.users.models import User, AGENT, STUDENT
from eduwise.utils.logging.logger import logger


class BaseTestCase(APITestCase):
    @staticmethod
    def ok(msg=''):
        logger.log(1, msg + ": PASSED")

    @classmethod
    def setUpTestData(cls) -> None:
        cls.admin_json = {'username': 'admin', 'password': 'mweobfOJE_EBVknckejbcec'}
        cls.admin = User.objects.create_superuser(**cls.admin_json)
        # cls.assertTrue(cls.admin.is_superuser)

        cls.agent_json = {'username': 'agent', 'password': 'lfkbvwoefbqnfewDJEBD__ECIEBE', 'role': AGENT}
        cls.agent = User.objects.create_user(**cls.agent_json)
        # cls.assertTrue(cls.agent.is_agent)

        cls.student_json = {'username': 'student', 'password': 'ecjwbeNDOEBO_ENCIJEBD#', 'role': STUDENT}
        cls.student = User.objects.create_user(**cls.student_json)
        # cls.assertTrue(cls.student.is_student)

        cls.client = APIClient()
        cls.ok('Test case setup')

        response = cls.client.post('/api/auth/jwt/create/', data={'username': cls.admin_json['username'],
                                                                  'password': cls.admin_json['password']})

        print(response)
        cls.admin_token = response.data['access']
        cls.admin_auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + cls.admin_token,
        }
        cls.ok('Admin login')
