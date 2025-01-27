from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import FilmModel
from ..serializers import FilmSerializer


class FilmView(ReadOnlyModelViewSet):
    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [AllowAny]
