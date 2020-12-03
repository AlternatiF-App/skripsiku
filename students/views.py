from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .pagination import *
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

        max1 = par1[0];
        for i in range(0, len(par1)):
            if (par1[i] > max1):
                max1 = par1[i];
        min1 = par1[0];
        for i in range(0, len(par1)):
            if (par1[i] < min1):
                min1 = par1[i];

        max2 = par2[0];
        for i in range(0, len(par2)):
            if (par2[i] > max2):
                max2 = par2[i];
        min2 = par2[0];
        for i in range(0, len(par2)):
            if (par2[i] < min2):
                min2 = par2[i];

        max3 = par3[0];
        for i in range(0, len(par3)):
            if (par3[i] > max3):
                max3 = par3[i];
        min3 = par3[0];
        for i in range(0, len(par3)):
            if (par3[i] < min3):
                min3 = par3[i];

        k = 3
        C_x = [max1, min2, min3]
        C_y = [min1, max2, min3]
        C_z = [min1, min2, max3]
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

class StudentsUpdateClusterList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LargeResultsSetPagination

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = StandardResultsSetPagination

class StudentsListByUser(generics.ListAPIView):
    serializer_class = StudentSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        teacher = self.kwargs['teacher']
        return Student.objects.filter(teacher__username=teacher)

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)