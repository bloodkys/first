from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        "name1": "김영석",
        "name2": "홍길동",
        "name3": "아무개",
        "food": "연어초밥",
        "hobby": "음악감상",
        "interest": "게임",
    }
    # render(html파일을 연결시켜주는 라이브러리)
    return render(request, "it/home.html", context)
