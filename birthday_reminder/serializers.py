from rest_framework import serializers
from .models import Group, Contact

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class ContactSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    
    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'nickname', 'group', 'birth_date', 'active']
