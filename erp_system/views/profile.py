from rest_framework.generics import RetrieveAPIView
from django.contrib.auth import get_user_model
from erp_system.serializers.profile import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
User = get_user_model()


class ProfileUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user

