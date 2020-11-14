from rest_framework import serializers
from students.models import Student
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView
)

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Student
        fields = ['id', 'teacher', 'fullname', 'id_minat', 'student_class',
                'score_math', 'score_science', 'score_indonesian', 'cluster']

class ClustersSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=True)
    class Meta(object):
        model = Student
        fields = ['id', 'cluster']
        list_serializer_class = BulkListSerializer