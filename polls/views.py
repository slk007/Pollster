from django.shortcuts import render, get_object_or_404, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

# Create your views here.

def index(requests):

    question_list = Question.objects.order_by('-pub_date')
    context = {'question_list': question_list}

    return render(requests, 'polls/index.html', context)


def detail(requests, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Questions does not exist")
    return render(requests, 'polls/detail.html', {'question':question})

def results(requests, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(requests, "polls/results.html", {"question": question})

def vote(requests, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))