from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Function
@registry.register_document
class FunctionDocument(Document):
    class Index:
        name = 'functions'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Function
        fields = ['name', 'call_spec', 'description', 'args', 'examples']