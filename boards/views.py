from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, DeleteView
from .models import Board
from django.urls import reverse_lazy, reverse
from .forms import BoardForm
from django.http import HttpResponse

# Create your views here.
# 추후 로그인 리콰이어

# APIView는 RESTful API를 만들기 위해 Djnago에서 제공하는 클래스 기반 뷰 중 하나
# RESTful API를 작성하는 데 필요한 다양한 기능을 제공한다.
# 요청과 응답을 직렬화하는 Serializer, 이증과 권한을 다루는 Permission 및 Authentication 클래스 등을 제공
# 각 HTTP 메서드(get,post,put,delete 등)에 대한 기본적인 구현을 제공
# 이를 오버라이드하여 원하는 기능을 구현 가능
# 그래서 APIView를 사용
class Boards(View):
    def get(self, request):
        form = BoardForm()
        return render(request, 'board/create_board.html', {'form': form})

    def post(self, request):
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            # board.author
            board.save()

            return redirect('/board/list/')

    def delete(self, request, board_id):
        Board.objects.get(board_id=board_id).delete()
        return redirect('/board/list/')


class BoardList(View):
    def get(self, request):
        if request.method == 'GET':
            boards = Board.objects.all().order_by('-updated_at')
            return render(request, 'board/board_list.html', {'boards': boards})
        return redirect('/board/')


# 게시글 이미지는 나중에 넣기? 관련 뷰가 있던 것 같음
