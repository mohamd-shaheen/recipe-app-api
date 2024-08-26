from decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase
from core import models


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        email = "test@example.com"
        password = "testpassword"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):

        email_samples = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@EXAMPLE.COM', 'test4@example.com'],
        ]

        for email, expected in email_samples:
            user = get_user_model().objects.create_user(
                email=email,
                password='12345'
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_ValueError(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email="test1@example.com",
            password='12345'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_recipe(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='123456'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='test title',
            description='test description',
            price=Decimal('6.7'),
            time_minutes=5,
        )

        self.assertEqual(str(recipe), recipe.title)
