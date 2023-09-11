from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html',context)
    #return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id) #pk에 해당하는 건이 없으면 오류 대신 404 페이지를 반환
    content = {'question':question}
    return render(request, 'pybo/question_detail.html',content)
