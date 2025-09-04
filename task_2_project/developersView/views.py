from django.shortcuts import render

# Create your views here.
Develpers = [
    {
        "username": "hassan",
        "first_name": "Hassan",
        "last_name": "Kabirian",
        "skills": ["Python", "Django", "Vue.js"],
    },
    {
        "username": "sara",
        "first_name": "Sara",
        "last_name": "Ahmadi",
        "skills": ["JavaScript", "React", "CSS"],
    },
    {
        "username": "ali",
        "first_name": "Ali",
        "last_name": "Rezayi",
        "skills": ["Java", "Spring Boot", "SQL"],
    },
]


def DevelopersListView(request):
    if request.method == "GET":
        context = {'developers': Develpers}
        pass


def DeveloperCV_View(request, username):
    if request.method == "GET":
        for dev in Develpers:
            if dev['username'] == username:
                context = {"developer": dev}
                pass
