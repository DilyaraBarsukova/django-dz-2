from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def menu(request, a):
    servings = int(request.GET.get("servings", 1))
    b = {}
    for x in range(len(DATA[a])):
        b[list(DATA[a])[x]] = float(dict(DATA[a])[list(DATA[a])[x]])*servings
    context = {
        'recipe':
            b
    }
    print(a)
    return render(request, 'calculator/index.html', context)
