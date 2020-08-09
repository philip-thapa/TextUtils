# I've created this file - philip
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    newText = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('uppercase','off')
    newlineremoval = request.POST.get('newlineremoval','off')
    extarspaceremoval = request.POST.get('extarspaceremoval', 'off')
    countCharacter  = request.POST.get('countCharacter', 'off')

    if removepunc == "on":
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in newText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        newText = analyzed
        # return render(request, 'analyze.html', params)

    if capitalize == 'on':
        analyzed = ''
        for char in newText:
            analyzed += char.upper()
        params = {'purpose':'Changed into Upper case', 'analyzed_text':analyzed}
        newText = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremoval == 'on':
        analyzed = ''
        for char in newText:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'New line removal', 'analyzed_text': analyzed}
        newText = analyzed
        # return render(request, 'analyze.html', params)

    if extarspaceremoval == 'on':
        analyzed = ''
        for index, char in enumerate(newText):
            if not(newText[index] == '' and newText[index+1] == ''):
                analyzed += char
        params = {'purpose': 'Extra space removal', 'analyzed_text': analyzed}
        newText = analyzed
        # return render(request, 'analyze.html', params)

    if countCharacter == 'on':
        analyzed = len(newText)
        params = {'purpose': 'Total no of characters', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if (removepunc != 'on' and capitalize != 'on' and newlineremoval != 'on' and extarspaceremoval != 'on' and countCharacter != 'on'):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)



