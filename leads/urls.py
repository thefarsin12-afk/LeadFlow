from django.urls import path

from leads.views import LeadsListCreateView
from leads.views import LeadsRetriveUpdateDeleteView

urlpatterns = [

    path('leads/',LeadsListCreateView.as_view()),

    path('leads/<int:pk>/',LeadsRetriveUpdateDeleteView.as_view()),


]