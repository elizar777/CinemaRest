from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name',
                  'last_name', 'date_joined')
        
class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        max_length=255, write_only=True
    )

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name',
                  'phone', 'password', 'confirm_password')
        
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        print(attrs)
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password':'Длина пароля меньше 8 символов'})
        return attrs