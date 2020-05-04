from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteSuite(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@django-project.com',
            password='Test@12345'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='taimoorpasha2009@gmail.com',
            password='Test@12345',
            name='Taimoor Pasha'
        )

    def test_users_listed(self):
        """Test user are listed on user page."""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)
        status_code = response.status_code
        if status_code == 200:
            self.assertContains(response, self.user.name)
            self.assertContains(response, self.user.email)
        return ValueError(status_code)

    def test_user_change_page(self):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test That the create user page works"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
