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
        return render(request=request, template_name="developersView/listView.html", context=context)


def DeveloperCV_View(request, username):
    if request.method == "GET":
        for dev in Develpers:
            if dev['username'] == username:
                context = {"developer": dev}
                return render(request=request, template_name="developersView/CV_View.html", context=context)

        error = f'Developers named {username} doesnt find'
        context = {'error': error}
        return render(request=request, template_name="developersView/CV_View.html", context=context)
