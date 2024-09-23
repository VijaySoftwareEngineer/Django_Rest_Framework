# GenricAPIView and model mixin

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# List and Create pk is not required
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # for GET and POST method
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    # Retrive, Update and Destroy- pk is required
    
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # for Retrive
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    # for Update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    # for Destroy
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)