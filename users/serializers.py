from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "email", "first_name", "last_name", "date_joined",
                  "phone_number", "birth_date", "is_female")
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ("date_joined",)

