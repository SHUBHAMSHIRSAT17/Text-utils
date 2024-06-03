from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get("text", "default")
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    nlr = request.POST.get("nlr", "off")
    esr = request.POST.get("esr", "off")
    nr = request.POST.get("nr", "off")
    print(djtext)
    print(removepunc)
    print(fullcaps)
    print(nlr)
    print(esr)
    print(nr)
    params_list = []

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        params_list.append(params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'smallcase to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        params_list.append(params)

    if nlr == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Avoid New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        params_list.append(params)

    elif esr == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if char == djtext[-1]:
                if not (djtext[index] == " "):
                    analyzed += char
            elif not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        params_list.append(params)

    if nr == "on":
        analyzed = ""
        numbers = '0123456789'
        for char in djtext:
            if char not in numbers:
                analyzed += char
        params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}
        djtext = analyzed
        params_list.append(params)

    if not any(op == "on" for op in [removepunc, fullcaps, nlr, esr, nr]):
        return HttpResponse("Please select any one operation and try again")

    return render(request, 'analyze.html', {'params_list': params_list})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


