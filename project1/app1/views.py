from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def ex1(request):
    a= request.GET.get('text','default')
    print(a)
    return HttpResponse('<h1>Hellow</h1><a href="www.youtube.com">youtube</a>')

def prac(request):
    return render(request,'prac1.html')

def ex2(request):
    text= request.POST.get('text')
    rpunck= request.POST.get('rpunc')
    nline= request.POST.get('nline')
    cap= request.POST.get('cap')
    rspace= request.POST.get('rsapce')
    
    out=''
    if rpunck=='on':
        punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in text:
            if i not in punc:
                out = out + i
        text=out
        out=''
    if(nline == 'on'):
        for i in text:
            if i !='\n' and i !='\r':
                out = out + i
        text=out
        out=''
    if(cap == 'on'):
        for i in text:
            out = out + i.upper()
        text=out
        out=''
    if(rspace == 'on'):
        for i in text:
            if i !=' ':
                out = out + i
        text=out
        out=''
    dic={"text":text}
    return render(request,'out.html',dic)

def index(request):
    return render(request,'index.html')