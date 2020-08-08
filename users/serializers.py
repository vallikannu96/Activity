from rest_framework import serializers
from users.models import ActivityPeriods, ActivityUsers
from datetime import datetime

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityUsers
        fields = ('id', 'real_name', 'tz')


class ActivitySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        primitive_repr = super(ActivitySerializer, self).to_representation(instance)
        if 'start_time' in primitive_repr:
            d = datetime.strptime(primitive_repr['start_time'], '%Y-%m-%dT%H:%M:%SZ')
            primitive_repr['start_time'] = d.strftime("%b %d %Y, %I:%M %p")
        if 'end_time' in primitive_repr:
            d = datetime.strptime(primitive_repr['end_time'], '%Y-%m-%dT%H:%M:%SZ')
            primitive_repr['end_time'] = d.strftime("%b %d %Y,  %I:%M %p")

        return primitive_repr

    class Meta:
        model = ActivityPeriods
        fields = ('id', 'start_time', 'end_time')


