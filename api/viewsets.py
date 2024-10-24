from rest_framework.viewsets import ModelViewSet
from api.models import Worklist
from api.serializers import WorklistSerializer

class WorklistViewSet(ModelViewSet):
    queryset = Worklist.objects.all()
    serializer_class = WorklistSerializer
