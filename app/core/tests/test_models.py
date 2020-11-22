from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='jackyfeng1218@gmail.com', password='password'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'jacky@gmail.com'
        password = 'password@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        # helper function from django user model
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'jacky@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creatig user with no email raises error """
        with self.assertRaises(ValueError):
            # code within the block should raise given error
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'jacky@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Test the tag string representation """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """ Test the ingredient string representation """
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """ Test the recipe string representation """
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='shui zhu yu',
            time_minutes=5,
            price=5.00,
        )

        self.assertEqual(str(recipe), recipe.title)
