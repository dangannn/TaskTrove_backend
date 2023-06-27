from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import News

CustomUser = get_user_model()


class NewsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем пользователя для новости
        user = CustomUser.objects.create_user(username='testuser', password='testpassword')

        # Создаем новость
        News.objects.create(author=user, name='Test News', description='This is a test news.')

    def test_news_author(self):
        news = News.objects.get(id=1)
        expected_author = CustomUser.objects.get(username='testuser')
        self.assertEqual(news.author, expected_author)

    def test_news_name(self):
        news = News.objects.get(id=1)
        expected_name = 'Test News'
        self.assertEqual(news.name, expected_name)

    def test_news_description(self):
        news = News.objects.get(id=1)
        expected_description = 'This is a test news.'
        self.assertEqual(news.description, expected_description)
