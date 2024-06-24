from django.urls import path
from .views import IndexView, EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView, PastEventListView, CalendarView

app_name = 'events'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/past/', PastEventListView.as_view(), name='past_event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/new/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('calendar/', CalendarView.as_view(), name='calendar_view'),
]
