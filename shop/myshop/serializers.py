from rest_framework import serializers
from .models import Items

class ShopSerializers(serializers.ModelSerializers):
    class Meta:
        model=Items
        fields='__all__'