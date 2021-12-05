from rest_framework import serializers

from control.models import Control

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ['id', 'book_text', 'loan_date', 'url_image', 'name_user', 'description']