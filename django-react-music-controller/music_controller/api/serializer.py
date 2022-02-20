"""
Created by cyborgoat at 2022/2/20
Email: cyborgoat@outlook.com

Description
-----------

"""
from rest_framework import serializers

from api.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
