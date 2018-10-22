import datetime
from haystack import indexes
from .models import School


class SchoolIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    city = indexes.CharField(model_attr='city')
    board = indexes.CharField(model_attr='board')

    def get_model(self):
        return School

