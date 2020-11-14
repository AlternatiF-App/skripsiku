from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from copy import deepcopy
import numpy as np
from rest_framework import permissions

class UpdateCluster(ListBulkCreateUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = ClustersSerializer

class GetClusters(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        par1 = queryset.values_list('score_math', flat=True)
        par2 = queryset.values_list('score_science', flat=True)
        par3 = queryset.values_list('score_indonesian', flat=True)

        X = np.array(list(zip(par1, par2, par3)))

        def dist(a, b, ax=1):
            return np.linalg.norm(a - b, axis=ax)

        k = 3
        C_x = [76, 62, 62]
        C_y = [69, 77, 69]
        C_z = [64, 64, 73]
        C = np.array(list(zip(C_x, C_y, C_z)), dtype=np.int)

        C_old = np.zeros(C.shape)
        clusters = np.zeros(len(X))
        error = dist(C, C_old, None)
        while error != 0:
            for i in range(len(X)):
                distances = dist(X[i], C)
                cluster = np.argmin(distances)
                clusters[i] = cluster
            C_old = deepcopy(C)
            for i in range(k):
                points = [X[j] for j in range(len(X)) if clusters[j] == i]
                C[i] = np.mean(points, axis=0)
            error = dist(C, C_old, None)

        return Response({"clusters":clusters})

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)