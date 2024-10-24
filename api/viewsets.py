from rest_framework.viewsets import ModelViewSet
from api.models import Worklist
from api.serializers import WorklistSerializer
from drf_spectacular.utils import extend_schema

#@extend_schema(exclude=True)
class WorklistViewSet(ModelViewSet):
    queryset = Worklist.objects.all()
    serializer_class = WorklistSerializer
