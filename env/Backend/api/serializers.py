from rest_framework import serializers
from .models import Registration, Standard, Division ,Staff
from django.contrib.auth.hashers import make_password

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
      model = Registration
      fields = ['name', 'email', 'birth_date','role', 'password', 'confirm_password']
      extra_kwarg = {
        'password': {'write_only': True, 'required': True},
        'confirm_password':{'write_only' : True, 'required':True},
      }
    
    def validate(self, data):

      if data['password'] != data['confirm_password']:
          raise serializers.ValidationError({"confirm_password": "Passwords must match."})
      return data

    def create(self, validated_data):
        user = Registration(role=validated_data['role'])
        validated_data.pop('confirm_password', None)
        return super().create(validated_data)

    
    
    
class LoginSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  password = serializers.CharField(max_length=255)
    
    
    
class StandardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Standard
    fields = ['id','StandardName']
    
class DivisionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Division
    fields = '__all__'
    
    
class StaffSerializer(serializers.ModelSerializer):
    forkey = RegistrationSerializer()

    class Meta:
        model = Staff
        fields = ['mobile', 'Qualification', 'forkey']

    def create(self, validated_data):
        registration_data = validated_data.pop('forkey')  
        registration_instance = Registration(**registration_data)  
        registration_instance.save()  
        staff_instance = Staff.objects.create(forkey=registration_instance, **validated_data)
        return staff_instance