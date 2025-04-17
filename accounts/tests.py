from django.test import TestCase, Client
from django.urls import reverse
from .models import Account

class AccountTests(TestCase):
    def setUp(self):
        # Set up test URLs
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        
        # Test user data
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'TestPass123',
            'confirm_password': 'TestPass123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone_number': '09123456789'
        }
        
        # Create a test user
        self.test_user = Account.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        self.test_user.is_active = True
        self.test_user.save()

    def test_login_valid_credentials(self):
        """Test login with valid credentials"""
        login_data = {
            'email': 'testuser@example.com',
            'password': 'TestPass123'
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 302)  # Should redirect after successful login
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        login_data = {
            'email': 'wrong@example.com',
            'password': 'WrongPass123'
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 200)  # Should stay on login page
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_register_valid_data(self):
        """Test registration with valid data"""
        test_user_data = {
            'username': 'newuser',  # username متفاوت از کاربر قبلی
            'email': 'newuser@example.com',  # email متفاوت از کاربر قبلی
            'password': 'TestPass123',
            'confirm_password': 'TestPass123',
            'first_name': 'New',
            'last_name': 'User',
            'phone_number': '09123456789'
        }
        response = self.client.post(self.register_url, test_user_data)
        print(response.content)  # برای دیباگ
        self.assertEqual(response.status_code, 302)  # باید به صفحه لاگین ریدایرکت شود
        self.assertTrue(Account.objects.filter(email='newuser@example.com').exists())

    def test_register_password_mismatch(self):
        """Test registration with mismatched passwords"""
        self.user_data['confirm_password'] = 'DifferentPass123'
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 200)  # Should stay on registration page
        self.assertContains(response, "رمز عبور و تایید آن مطابقت ندارند")
