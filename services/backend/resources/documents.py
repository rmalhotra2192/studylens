from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Resource, Book, Video, Course


@registry.register_document
class ResourceDocument(Document):
    class Index:
        name = "resources"

    class Django:
        model = Resource

    title = fields.TextField(attr="title")
    description = fields.TextField(attr="description")


@registry.register_document
class BookDocument(ResourceDocument):
    class Index:
        name = "books"

    class Django:
        model = Book

    isbn = fields.TextField(attr="isbn")
    authors = fields.TextField(attr="authors")


@registry.register_document
class VideoDocument(ResourceDocument):
    class Index:
        name = "videos"

    class Django:
        model = Video

    video_id = fields.TextField(attr="video_id")


@registry.register_document
class CourseDocument(ResourceDocument):
    class Index:
        name = "courses"

    class Django:
        model = Course

    course_id = fields.TextField(attr="course_id")
