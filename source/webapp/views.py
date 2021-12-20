from django.shortcuts import render

# Create your views here.
from webapp.control import ControlGame


def game(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        while True:
            num = request.POST.get("first").strip().split(' ')
            num_int = []

            for i in num:
                num_int.append(int(i))
            a = ControlGame(num_int)

            print(a.bulls)
            print(a.cows)

            context = {
                'bulls': a.bulls,
                'cows': a.cows,
                'player': a.player_nums,
                'secret': a.secret_nums,
                'history': a.history,
                'errors': ""
            }
            if not a.check_len():
                context['errors'] += "enter exactly 4 numbers"
            if not a.number_size():
                context['errors'] += "enter exactly from 1 to 10"

            return render(request, 'index.html', context)
