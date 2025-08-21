from django.shortcuts import render

# Create your views here.


Develpers=[
    {
        "username":"hassan",
        "first_name":"Hassan",
        "last_name":"Kabirian",
        "skills":["Python","Django","Vue.js"],
    },
    {
        "username":"sara",
        "first_name":"Sara",
        "last_name":"Ahmadi",
        "skills":["JavaScript","React","CSS"],
    },
    {
        "username":"ali",
        "first_name":"Ali",
        "last_name":"Rezayi",
        "skills":["Java","Spring Boot","SQL"],
    },
]


def listDevelporsView(request):
    if request.method=="GET":
        content={"developers":Develpers}
        return render()



def CV_View(request,username):
    if request.method=="GET":
        for dev in Develpers:
            if dev["username"]==username:
                content={'developer':dev}
                return render()
        content={"error":f"DONT FIND DEVELOPER NAMED {username}"}
        return render()
