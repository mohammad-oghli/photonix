from pathlib import Path

from django.utils import timezone
import factory

from photonix.accounts.models import User
from photonix.photos.models import Library, LibraryUser, Photo, PhotoFile, Tag, PhotoTag, Task


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'test'


class LibraryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Library

    name = factory.Sequence(lambda n: f'Test Library {n}')


class LibraryUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LibraryUser

    library = factory.SubFactory(LibraryFactory)
    user = factory.SubFactory(UserFactory)
    owner = True


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    library = factory.SubFactory(LibraryFactory)


class PhotoFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PhotoFile

    photo = factory.SubFactory(PhotoFactory)
    path = str(Path(__file__).parent / 'photos' / 'snow.jpg')
    mimetype = 'image/jpeg'
    bytes = 1000
    file_modified_at = factory.LazyAttribute(lambda o: timezone.now())


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    library = factory.SubFactory(LibraryFactory)
    name = factory.Sequence(lambda n: f'Tag {n}')


class PhotoTagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PhotoTag

    photo = factory.SubFactory(PhotoFactory)
    tag = factory.SubFactory(TagFactory)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    type = 'classify.style'
    status = 'P'
