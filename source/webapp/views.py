from django.shortcuts import render

# Create your views here.
from webapp.control import ControlGame


def game(request):
    global numbers
    numbers = []

    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':

        while True:
            num = request.POST.get("first").strip().split(' ')
            num_int = []
            numbers.append(num_int)
            for i in num:
                num_int.append(int(i))
            a = ControlGame(num_int)
            print(a.bulls)
            print(a.cows)
            print(numbers)
            context = {
                'bulls': a.bulls,
                'cows': a.cows,
                'player': a.player_nums,
                'secret': a.secret_nums
            }
            return render(request, 'index.html', context)
