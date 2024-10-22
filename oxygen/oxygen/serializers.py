from rest_framework import serializers
from .models import permission, EntryForm
class permissionserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=permission
		fields=('ParentsApproval','ClasscoordinatorApproval','WardenApproval','HODApproval')

class EForm(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = EntryForm
		fields = ('Project', 'Task')