from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def setUp(self) -> None:
        self.user_items = {
            "username": "test",
            "email": "test@test.com",
            "password": "test@123"
        }
        self.super_user_items = {
            "username": "superuser",
            "email": "superuser@test.com",
            "password": "test@123"
        }
        self.user = None
        self.super_user = None
        return super().setUp()
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(**self.user_items)
        self.assertEqual(user.username, self.user_items.get("username"))
        self.assertEqual(user.email, self.user_items.get("email"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(**self.super_user_items)
        self.assertEqual(admin_user.username, self.super_user_items.get("username"))
        self.assertEqual(admin_user.email, self.super_user_items.get("email"))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    
