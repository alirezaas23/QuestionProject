from django.shortcuts import render, get_object_or_404, reverse
from . import models
from django.views import generic
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return models.Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    template_name = 'app/detail.html'
    model = models.Question

class ResultView(generic.DetailView):
    template_name = 'app/result.html'
    model = models.Question

def vote(request, question_id):
    question=get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, models.Choice.DoesNotExist):
        return render(request, 'app/detail.html', context={
            'question':question,
            'error':'You Don`t Choose A Choice!',
        })
    else:
        selected_choice.vote+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('result', args=(question.id, )))
