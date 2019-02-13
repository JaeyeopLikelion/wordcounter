from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.POST['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    Max = 0
    Max_Key = ""
    for word, howmany in word_dictionary.items():
        if howmany > Max:
            Max = howmany
            Max_Key = word

    length = len(text)
    if not "choice" in request.POST:
        length = length - len(words) + 1

    return render(request, 'result.html', {'full': text, 'total' : length, 'dictionary' : word_dictionary.items(), 'max_value': Max, 'max_key': Max_Key})