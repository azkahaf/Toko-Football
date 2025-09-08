from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406435805',
        'name': 'Harish Azka Firdaus',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
