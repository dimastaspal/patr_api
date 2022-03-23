from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from patr_api_app.serializers import AllNewsSerializer, AllStaffSerializer, AllEventsSerializer, AllDocsSerializer, \
    AllPartnersSerializer, AllVideosSerializer, AllParkSerializer

from patr_api_app.models import News, Events, Staff, Partners, Documents, Videos, Park


class AllNewsView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = AllNewsSerializer


class AllEventsView(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = AllEventsSerializer


class AllStaffView(ModelViewSet):
    queryset = Staff.objects.filter(position = 23)
    serializer_class = AllStaffSerializer


class AllDocsView(ModelViewSet): #documents или docsType в models
    queryset = Documents.objects.all()
    serializer_class = AllDocsSerializer


class AllPartnersView(ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = AllPartnersSerializer


class AllVideosView(ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = AllVideosSerializer


class AllParkView(ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = AllParkSerializer

def index (request):
    return render(request, 'index.html')
