from rest_framework import viewsets
from .serializers import permissionserializer, EForm
from .models import permission, EntryForm
class permissionviewset(viewsets.ModelViewSet):
	queryset=permission.objects.all()
	serializer_class=permissionserializer

class EForm_views(viewsets.ModelViewSet):
	queryset=EntryForm.objects.all()
	serializer_class=EForm