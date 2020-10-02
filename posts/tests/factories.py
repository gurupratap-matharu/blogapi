import factory
from django.contrib.auth.models import User
from posts.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    author = factory.SubFactory(UserFactory)
    title = factory.Faker('catch_phrase')
    body = factory.Faker('text')
