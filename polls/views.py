from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from polls.models import Question, Choice

class HomeView(View):
    def get(self, request):
        poll = Question.objects.all()
        ctx = { 'poll_list' : poll }
        return render(request, 'polls/home.html', ctx)


class NewPoll(CreateView):
    model = Question
    success_url = reverse_lazy('polls:home')
    fields = '__all__'
