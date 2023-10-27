from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from main.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='test_course',
            description='test_course_desc'
        )

        self.lesson = Lesson.objects.create(
            title='Test_lesson',
            course=self.course,
            description='test'
        )

    def test_create_lesson(self):
        data = {
            'title': self.lesson.title,
            'course': self.course.id,
            'description': self.lesson.description,
        }
        response = self.client.post(
            '/lesson/create',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': (self.lesson.id + 1),
             'title': self.lesson.title,
             'description': self.lesson.description,
             'preview': None,
             'link': None,
             'course': self.course.id, }
        )
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        response = self.client.get(
            'lesson/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()['results'],
            [{'id': self.lesson.id,
              'title': self.lesson.title,
              'description': self.lesson.description,
              'preview': None,
              'link': None,
              'course': self.course.id, }]
        )

    def test_retrieve_lesson(self):
        response = self.client.get(
            f'lesson/{self.lesson.id}'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'id': self.lesson.id,
             'title': self.lesson.title,
             'description': self.lesson.description,
             'preview': None,
             'link': None,
             'course': self.course.id, }
        )

    def test_update_lesson(self):
        data = {
            'title': 'Test_updated_lesson',
        }
        response = self.client.patch(
            f'lesson/update/{self.lesson.id}',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'id': self.lesson.id,
             'title': self.lesson.title,
             'description': self.lesson.description,
             'preview': None,
             'link': None,
             'course': self.course.id, }
        )

    def test_destroy_lesson(self):
        response = self.client.delete(
            f'lesson/delete/{self.lesson.id}',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def tearDown(self):
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Subscription.objects.all().delete()


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='test_course',
            description='test_course_desc'
        )
        self.subs = Subscription.objects.create(
            course=self.course,
        )

    def test_create_subscription(self):
        data = {
            'course': self.course.id,
        }
        response = self.client.post(
            'subscription/create',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': (self.subs.id + 1), 'user': self.user.id, 'course': self.course.id}
        )
        self.assertTrue(
            Subscription.objects.all().exists()
        )

    def test_destroy_subscription(self):
        response = self.client.delete(
            f'subscription/delete/{self.subs.id}',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def tearDown(self):
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Subscription.objects.all().delete()
