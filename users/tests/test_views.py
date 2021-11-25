# from utils.tests import BaseTestCase
#
#
# class UserTest(BaseTestCase):
#
#     def test_student_register_api(self):
#         json = self.student_json
#         json['username'] = 'random_student'
#         response = self.client.post('/api/auth/users/', data=self.student_json)
#         # print(type(response.data))
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data['role'], 'S')
#         self.ok('Student register')
#
#     def test_get_student_details(self):
#         response = self.client.get(f'/api/auth/users/{self.student.id}/', **self.admin_auth_headers)
#         self.assertEqual(response.status_code, 200)
#         data = response.data
#         # Assert password is not included in details
#         self.assertIsNone(data.get('password', None))
#         for k, v in self.student_json.items():
#             # exclude password in get
#             if k != 'password':
#                 self.assertEqual(v, data[k])
#
#         self.ok('Student details')
#
#     def test(self):
#         pass
