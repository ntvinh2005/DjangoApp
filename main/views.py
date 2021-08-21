
from .models import Note,Item,Date,Topic
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreateNewSub
from datetime import date
# Create your views here.

def index(response,id):
    note=Note.objects.get(id=id)
    today = date.today()
    if response.method=="POST":
        print(response.POST)
        if response.POST.get("newItem"):
            txt=response.POST.get("new")          
            if len(txt)>2:             
                note.item_set.create(text=txt)
                for dat in note.date_set.all():
                    dat.text=str(today.day)+"/"+str(today.month)+"/"+str(today.year)
                    dat.save()
            else:
                print("Try again!")     
        elif response.POST.get("delete")  :
            note.delete() 
            return redirect("/view")    
        elif response.POST.get("update")  : 
            for item in note.item_set.all():
                item.text=response.POST.get("o"+str(item.id))  
                item.save() 
            for dat in note.date_set.all():
                dat.text=str(today.day)+"/"+str(today.month)+"/"+str(today.year)
                dat.save()                            
    return render(response,"main/note.html",{"note":note })

def home(response):
    return render(response,"main/home.html",{})

def subject(response):
    if response.method=="POST": 
        form=CreateNewSub(response.POST)
        today=date.today()
        s=""
        if form.is_valid():
            n=form.cleaned_data["name"]
            a=form.cleaned_data["learning"]
            b=form.cleaned_data["working"]
            c=form.cleaned_data["idea"]
            d=form.cleaned_data["life"]
            t=Note(name=n)
            t.save()
            t.date_set.create(text=str(today.day)+"/"+str(today.month)+"/"+str(today.year))   
            if a==True:
                s+="learning "
            if b==True:
                s+="working "
            if c==True:
                s+="idea " 
            if d==True:
                s+="life "  
            t.topic_set.create(text=s,learn=a,work=b,idea=c,life=d) 
            return redirect("/view")
    else:
        form=CreateNewSub()
    return render(response,"main/subject.html",{"form":form})

def view(response):
    notes=Note.objects.all()
    return render(response, "main/view.html",{"notes":notes})

def filter(response,fil):
    notes=Note.objects.all()
    return render(response, "main/filter.html",{"fil":fil,"notes":notes})        
