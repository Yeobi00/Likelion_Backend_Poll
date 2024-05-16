from rest_framework import serializers
from .models import Poll

class PollSerializer(serializers.ModelSerializer):
    agreeRate = serializers.SerializerMethodField()
    disagreeRate = serializers.SerializerMethodField()
    
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'agree', 'disagree', 'agreeRate', 'disagreeRate', 'createdAt']
    
    def get_agreeRate(self, obj):
        return obj.get_agreeRate()
    
    def get_disagreeRate(self, obj):
        return obj.get_disagreeRate()