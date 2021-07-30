import graphene
from graphene_django import DjangoObjectType
from .models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'excerpt') # We have access to these data, doesn't mean we are colleting these data

class Query(graphene.ObjectType):

    all_books = graphene.List(BookType)

    def resolve_all_books(root, info):
        # return Book.objects.all()
        return Book.objects.filter(title="django")

schema = graphene.Schema(query=Query)