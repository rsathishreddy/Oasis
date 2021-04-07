from rest_framework import serializers

from .models import Candidate


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'description')
