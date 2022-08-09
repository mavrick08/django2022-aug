from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render
import string
'''
This is my first function based view in django.
'''

def home_view(request):
    your_name = "dummy user"  #you are definfing the static data
    # return HttpResponse(f"Hello Your Name is {your_name}")
    mydict = {'name':your_name,'age':22}
    # return HttpResponse(mydict['age'])
    return render(request,'home.html',mydict)


def index_func(request):
    return render(request,'index.html')



def analyze_func(request):
    input_text = request.POST.get('inp_data')
    rm_punc = request.POST.get('rm_punc','off')
    full_caps = request.POST.get('full_caps','off')
    new_line_remover = request.POST.get('new_line_remover','off')
    space_remover = request.POST.get('space_remover','off')
    word_count = request.POST.get('word_count','off')


    if full_caps == "on":
        analyzed_text = ""
        for char in input_text:
            analyzed_text = analyzed_text+char.upper()
        # return HttpResponse(analyzed_text)
        my_result = {'action':analyzed_text}
        return render(request,'result.html',my_result)

    elif space_remover == "on":
        analyzed_text = input_text
        analyzed_text = analyzed_text.replace(" ","")
        my_result = {'action':analyzed_text}
        return render(request,'result.html',my_result)


    elif word_count == "on":
        count = 0
        for val in input_text:
            count+=1
        my_result = {'action':count}
        return render(request,'result.html',my_result)


    elif rm_punc == "on":
        str_punc = string.punctuation
        analyzed_text = ""
        for char in input_text:
            if char not in str_punc:
                analyzed_text = analyzed_text+char
        my_result = {'action':analyzed_text}
        return render(request,'result.html',my_result)

    elif new_line_remover == "on":
        analyzed_text = ""
        for char in input_text:
            if char !='\n' and char != '\r':
                analyzed_text = analyzed_text+char
        my_result = {'action':analyzed_text}
        return render(request,'result.html',my_result)