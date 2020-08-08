from rest_framework import viewsets,status
from rest_framework.permissions import  AllowAny
from users.models import ActivityUsers, ActivityPeriods
from users.serializers import UsersSerializer, ActivitySerializer
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = ActivityUsers.objects.all()
    serializer_class = ActivityUsers
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='get-activity-users')
    def get_activity_users(self, request):
        try:
            user_queryset = ActivityUsers.objects.filter(is_superuser=False)
            user_serializer = UsersSerializer(user_queryset, context={'request': request}, many=True).data
            for user in user_serializer:
                activity_qs = ActivityPeriods.objects.filter(user_id=user['id'])
                user['activity_periods'] = ActivitySerializer(activity_qs, context={'request': request}, many=True).data
            data = {
                "ok": True,
                "members": user_serializer
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            raise APIException("There was a problem!", e)


