from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django . urls import reverse
from django.template import Template, Context, loader
from .models import Question, Choice


def home(request):
    question = Question.objects.order_by('id').first()
    template = loader.get_template("quizz/index.html")
    context = {
        "question": question,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choices = Choice.objects.filter(question__id=question_id)
    context = {
        "question": question,
        "choices": choices,
    }
    return render(request, "quizz/detail.html", context)


def results(request, question_id, is_correct):
    question = get_object_or_404(Question, id=question_id)
    next_question = Question.objects.filter(id__gt=question_id).order_by(
        'id').first()
    choices = Choice.objects.filter(question__id=question_id)
    context = {
        "question": question,
        "next_question": next_question,
        "is_correct": is_correct,
        "choices": choices,
    }
    return render(request, "quizz/results.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'quizz/detail.html', {
            'question': question,
            'error_message': "Vous n'avez pas sélectionné de réponse.",
        })
    else:
        selected_choice.nb_votes += 1
        selected_choice.save()
        is_correct = selected_choice.correct
        return HttpResponseRedirect(reverse('quizz:results',
                                            args=(question.id, is_correct)))
