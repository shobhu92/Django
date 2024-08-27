from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    sentence = request.POST.get('text','')
    file = request.POST.get('file','')
    print(sentence)
    print(file)
    punctuations = '''!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    result_str = ""
    if sentence:
        for word in sentence:
            if word not in punctuations:
                result_str = result_str + word
    elif file:
        with open(file) as f:
            lines = f.readlines()
            for char in ''.join(lines):
                if char not in punctuations:
                    result_str = result_str + char

    print(result_str)
    params = {'result':result_str}
    #params = {'name':'Shobhit','Work':'Capgemini'}
    return render(request, 'index2.html',params)

def home(request):
    parm = {'YouTube':'https://www.youtube.com/',
            'Fb':'https://www.facebook.com/',
            'Insta':'https://www.instagram.com/'}
    return render(request,'home.html',parm)
