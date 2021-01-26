from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    """목록 출력"""
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')
    
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list' : page_obj}

    return render(request, 'papago/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question' : question}

    return render(request, 'papago/question_detail.html', context)