# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from dns import models,serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from deveops.api import WebTokenAuthentication
from rest_framework.pagination import PageNumberPagination


class DNSPagination(PageNumberPagination):
    page_size = 10


class DNSListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.DNS
    serializer_class = serializers.DNSSerializer
    queryset = models.DNS.objects.all()
    permission_classes = [AllowAny,]

    def get_queryset(self):
        from django.db.models import Q
        query = self.request.query_params.get('level', None)
        print(query)
        if query != "":
            if query == '1':
                return self.queryset.filter(father__isnull=True)
            elif query == '2':
                return self.queryset.filter(Q(father__father__isnull=True)&~Q(father__isnull=True))
            else:
                return self.queryset.exclude(Q(father__isnull=True)|Q(father__father__isnull=True))
        else:
            return self.queryset.all()


class DNSListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.DNS
    serializer_class = serializers.DNSSerializer
    queryset = models.DNS.objects.all().exclude(father__isnull=True)
    permission_classes = [AllowAny,]
    pagination_class = DNSPagination
    filter_fields = ('group',)

    def get_queryset(self):
        from django.db.models import Q
        query = self.request.query_params.get('level', None)
        if query != "":
            if query == '1':
                return self.queryset.filter(father__isnull=True)
            elif query == '2':
                return self.queryset.filter(Q(father__father__isnull=True)&~Q(father__isnull=True))
            else:
                return self.queryset.exclude(Q(father__isnull=True)|Q(father__father__isnull=True))
        else:
            return self.queryset.all()


class DNSCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.DNS
    serializer_class = serializers.DNSSerializer
    queryset = models.DNS.objects.all()
    permission_classes = [AllowAny,]

class DNSUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.DNS
    serializer_class = serializers.DNSSerializer
    queryset = models.DNS.objects.all()
    permission_classes = [AllowAny,]
    lookup_url_kwarg = 'pk'
    lookup_field = 'uuid'

class DNSDeleteAPI(WebTokenAuthentication, generics.DestroyAPIView):
    module = models.DNS
    serializer_class = serializers.DNSSerializer
    queryset = models.DNS.objects.all()
    permission_classes = [AllowAny,]
    lookup_url_kwarg = 'pk'
    lookup_field = 'uuid'