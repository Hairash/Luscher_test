from django.shortcuts import render


def index(request):
    # 1 — темно - синий
    # цвет;
    # 2 — сине - зеленый;
    # 3 — оранжево - красный;
    # 4 — желтый;
    # 5 — фиолетовый;
    # 6 — коричневый;
    # 7 — черный;
    # 0 — серый
    # цвет.
    #
    # Пример:
    # 07612453
    # 67543120
    return render(request, 'index.html', {'colors': colors})
colors = [
    [
        {'num': 1, 'color': '#1d36b4'},
        {'num': 2, 'color': '#339e8a'},
        {'num': 3, 'color': '#b06121'},
        {'num': 4, 'color': '#ffef42'},
        {'num': 5, 'color': '#7857ff'},
        {'num': 6, 'color': '#ba5921'},
        {'num': 7, 'color': '#000000'},
        {'num': 0, 'color': '#8a8a8a'},
    ],
    [
        {'num': 2, 'color': '#339e8a'},
        {'num': 6, 'color': '#ba5921'},
        {'num': 4, 'color': '#ffef42'},
        {'num': 0, 'color': '#8a8a8a'},
        {'num': 7, 'color': '#000000'},
        {'num': 5, 'color': '#7857ff'},
        {'num': 3, 'color': '#b06121'},
        {'num': 1, 'color': '#1d36b4'},
    ],
]
