from django.http import JsonResponse
from django.shortcuts import render

from .poems import data


def index(request):
    return render(request, 'index.html')


def regen(request, word_at):
    ret = data[int(word_at)].pop()
    data[int(word_at)].add(ret)
    return JsonResponse({'poem_name': ret[0], 'writer': ret[1], 'sentence': ret[2]})
