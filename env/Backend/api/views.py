from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Registration, Standard, Division, Staff
from . serializers import RegistrationSerializer,LoginSerializer, StandardSerializer, DivisionSerializer, StaffSerializer
from django.contrib.auth.hashers import check_password


class  RegistrationView(APIView):
  def get(self,request):
    query_set = Registration.objects.all()
    serializer = RegistrationSerializer(query_set, many=True)
    return Response(serializer.data)
    
  
  def post(self, request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
    
        try:
            user = Registration.objects.get(email=email)
        except Registration.DoesNotExist:
          
            print("User not found")  
            return Response({"error": "Email is not registered"}, status=status.HTTP_401_UNAUTHORIZED)
        

        if not check_password(password, user.password):
            print("Password does not match")  
            return Response({"error": "Please check password"}, status=status.HTTP_401_UNAUTHORIZED)
        
        user_role = user.role
        return Response({"message": "Login successful","role" : user_role}, status=status.HTTP_200_OK)

    
class StandardView(APIView):
  def get(self, request):
    query_set = Standard.objects.all()
    serializer = StandardSerializer(query_set,many = True)
    return Response(serializer.data,status=status.HTTP_200_OK)
  
  def post(self, request):
    serializer = StandardSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message" : "Standard created successfully"}, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
class StandardApi(APIView):
  def get(self,request,id):
    try:
      query_set = Standard.objects.get(id=id)
      serializer = StandardSerializer(query_set, many = False)
      return Response(serializer.data,status=status.HTTP_200_OK)
    except Standard.DoesNotExist:
      return Response({'message':'standard not found'},status=status.HTTP_200_OK)
  
  def put(self, request, id):
    try:
      standard = Standard.objects.get(id=id)
    except Standard.DoesNotExist:
      return Response({'message':'Standard not found'})
    serializer = StandardSerializer(standard, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message" : "Standard updated successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,id):
    try:
      standard = Standard.objects.get(id=id)
    except Standard.DoesNotExist:
      return Response({"message": "Standard not found"}, status=status.HTTP_404_NOT_FOUND)
    standard.delete()
    return Response({"message": "Standard deleted successfully"}, status=status.HTTP_200_OK)
    

class DivisionView(APIView):
  def get(self, request):
    query_set = Division.objects.all()
    serializer = DivisionSerializer(query_set, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self,request):
    serializer = DivisionSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message" : "Division created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)
  
class DivisionApi(APIView):
  def get(self,request,id):
    try:
      query_set = Division.objects.get(id=id)
      serializer = DivisionSerializer(query_set, many = False)
      return Response(serializer.data,status=status.HTTP_200_OK)
    except Division.DoesNotExist:
      return Response({'message':'division not found'},status=status.HTTP_200_OK)
    
  def put(self,request,id):
    try:
      division = Division.objects.get(id=id)
    except Division.DoesNotExist:
      return Response({'message': 'Division not found'},status=status.HTTP_204_NO_CONTENT)
    serializer = DivisionSerializer(division, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message" : "Division updated successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,id):
    try:
      division = Division.objects.get(id=id)
    except Division.DoesNotExist:
      return Response({"message": "Division not found"}, status=status.HTTP_404_NOT_FOUND)
    division.delete()
    return Response({"message": "Division deleted successfully"}, status=status.HTTP_200_OK)
  
  
class StaffView(APIView):
    def get(self, request):
        query_set = Staff.objects.all()
        serializer = StaffSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Staff created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffApi(APIView):
    def get(self, request, id):
        try:
            staff_member = Staff.objects.get(id=id)
            serializer = StaffSerializer(staff_member)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Staff.DoesNotExist:
            return Response({'message': 'Staff not found'}, status=status.HTTP_404_NOT_FOUND)
          
    def put(self, request, id):
      try:
          staff_member = Staff.objects.get(id=id)
      except Staff.DoesNotExist:
          return Response({'message': 'Staff not found'}, status=status.HTTP_404_NOT_FOUND)

      serializer = StaffSerializer(staff_member, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({"message": "Staff updated successfully"}, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            staff_member = Staff.objects.get(id=id)
        except Staff.DoesNotExist:
            return Response({'message': 'Staff not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StaffSerializer(staff_member, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Staff updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, id):
        try:
            staff_member = Staff.objects.get(id=id)
        except Staff.DoesNotExist:
            return Response({"message": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)

        staff_member.delete()
        return Response({"message": "Staff deleted successfully"}, status=status.HTTP_200_OK)