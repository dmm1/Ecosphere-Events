from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Event
from .forms import EventForm

class EventIndexView(TemplateView):
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.upcoming_events()[:5]
        context['past_events'] = Event.objects.past_events()[:5]
        return context

class CalendarView(TemplateView):
    template_name = 'events/calendar_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context

class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events/event_list.html'

    def get_queryset(self):
        return Event.objects.upcoming_events()

class PastEventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events/past_event_list.html'

    def get_queryset(self):
        return Event.objects.past_events()

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/event_detail.html'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
### fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'events/event_form.html'
    success_url = '/events/'

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
### fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'events/event_update_form.html'
    success_url = '/events/'

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = '/events/'
