from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_email(self):
        email = "taimoorpasha2009@gmail.com"
        password = "Test12345"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for new user is normalized"""
        email = "taimoorpasha@GMail.Com"
        user = get_user_model().objects.create_user(email,
                                                    'Test@1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test Creating user with no email raises value"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", 'Test@1234')

    def test_new_user_with_empty_password(self):
        """Test Creating user with empty password"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("taimoor.pasha@gmail.com", "    ")

    def test_new_user_with_empty_space(self):
        """Test Creating user with space"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(" ", "Test@1234")

    def test_new_create_superuser(self):
        """Test Creating a new user with super user rights"""
        user = get_user_model().objects.create_superuser(
            'taimoorpasha2009@gmail.com', 'Test@12345'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
