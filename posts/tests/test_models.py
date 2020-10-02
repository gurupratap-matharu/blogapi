from django.contrib.auth.models import User
from django.test import TestCase

from posts.models import Post


class PostTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            author=self.user,
            title='Life is beautiful',
            body='Live life each day as it comes'
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.author}', 'testuser')
        self.assertEqual(f'{post.title}', 'Life is beautiful')
        self.assertEqual(f'{post.body}', 'Live life each day as it comes')
