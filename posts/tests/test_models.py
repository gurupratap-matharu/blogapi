from django.contrib.auth.models import User
from django.test import TestCase
from posts.models import Post
from posts.tests.factories import PostFactory, UserFactory


class PostTests(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.post = PostFactory(author=self.user)

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.author}', self.user.username)
        self.assertEqual(f'{post.title}', self.post.title)
        self.assertEqual(f'{post.body}', self.post.body)
