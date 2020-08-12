from django.shortcuts import render

# 1 — темно - синий цвет;
# 2 — сине - зеленый;
# 3 — оранжево - красный;
# 4 — желтый;
# 5 — фиолетовый;
# 6 — коричневый;
# 7 — черный;
# 0 — серый цвет.
COLORS_MAP = {
    1: 'rgb(25, 0, 142)',
    2: 'rgb(0, 102, 0)',
    3: 'rgb(216, 0, 0)',
    4: 'rgb(190, 147, 0)',
    5: 'rgb(181, 0, 119)',
    6: 'rgb(103, 36, 1)',
    7: 'rgb(8, 8, 8)',
    0: 'rgb(112, 112, 112)',
}


def index(request):
    # Output example:
    # 07612453
    # 67543120

    # You can shuffle colors here
    color_packs = [
        [1, 2, 3, 4, 5, 6, 7, 0],
        [2, 6, 4, 0, 7, 5, 3, 1],
    ]
    colors = [
        [{'num': i, 'color': COLORS_MAP[i]} for i in color_pack] for color_pack in color_packs
    ]
    return render(request, 'index.html', {'colors': colors})
