# I have created my file-Gaurisha

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     s = '''<h1>Personal Navigator</h1> <br>
#            <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django Tutorial</a> <br>
#            <a href="https://www.viki.com/videos/1179725v">Chinese Drama</a>'''
#     return HttpResponse(s)
#
# def about(request):
#     return HttpResponse("About Gaurisha")


def index(request):
    return render(request, 'index2.html')

    # params = {'name':'gauri', 'place':'Mars'}
    # return render(request, 'index.html', params)

    # return HttpResponse("Home")

def analyze(request):
   # Get the text
   djtext = request.POST.get('text', 'default')

   # Check checkbox values
   removepunc = request.POST.get('removepunc', 'off')
   fullcaps = request.POST.get('fullcaps', 'off')
   extraspaceremover = request.POST.get('extraspaceremover', 'off')
   newlineremover = request.POST.get('newlineremover', 'off')
   # numberofchar = request.GET.get('number_of_char', 'off')

   # Check which checkbox is on
   if removepunc == "on":
      punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      analyzed = ""
      for char in djtext:
         if char not in punctuations:
            analyzed = analyzed + char

      params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
      djtext = analyzed
      # return render(request, 'analyze.html', params)

   if (fullcaps == "on"):
      analyzed = ""
      for char in djtext:
         analyzed = analyzed + char.upper()

      params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
      djtext = analyzed
      # Analyze the text
      # return render(request, 'analyze.html', params)

   if (extraspaceremover == "on"):
      analyzed = ""
      for index, char in enumerate(djtext):
         if not (djtext[index] == " " and djtext[index + 1] == " "):
            analyzed = analyzed + char

      params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
      djtext = analyzed
      # Analyze the text
      # return render(request, 'analyze.html', params)

   if (newlineremover == "on"):
      analyzed = ""
      for char in djtext:
         if char != "\n" and char != "\r":
            analyzed = analyzed + char
         else:
            print("no")
      print("pre", analyzed)
      params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

   # if (numberofchar == "on"):
   #    analyzed = 0
   #    for char in djtext:
   #       if not(char==" " or char=="," or char=="."):
   #          analyzed+=1
   #
   #    params = {'purpose': 'Number of characters in your text: ', 'analyzed_text': analyzed}
   #    # Analyze the text
   #    # return render(request, 'analyze.html', params)

   if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
      return HttpResponse("please select any operation and try again")

   return render(request, 'analyze2.html', params)

# def removepunc(request):
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("remove punc")
#
#     # return HttpResponse('''<h1>remove punc</h1>
#     #     <br>
#     #     <a href="/"><button>Back to home</button></a>''')
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")
#
#
#
