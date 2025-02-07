from django.shortcuts import render
from .models import get_random_text
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import TemplateForm


def template_view(request):
    if request.method == "GET":
        return render(request, 'app/template_form.html')

    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь

        # как пример получение данных по ключу `my_text`
        # my_text = received_data.get('my_text')

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            my_text = form.cleaned_data.get("my_text")  # Получили очищенные данные
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_email = form.cleaned_data.get("email")
            my_password = form.cleaned_data.get("password")
            my_date = form.cleaned_data.get("date")
            my_number = form.cleaned_data.get("number")
            my_checkbox = form.cleaned_data.get("checkbox")

            return JsonResponse(my_text, my_password, my_select, my_textarea
                                json_dumps_params={"ensure_ascii": False, "indent": 4}, safe=False)

        return render(request, 'app/template_form.html', context={"form": form})


        # # TODO Проведите здесь получение и обработку данных если это необходимо
        # my_password = received_data.get('password')
        #
        # # TODO Верните HttpRequest или JsonResponse с данными
        # return JsonResponse(my_password,
        #                     json_dumps_params={"ensure_ascii": False, "indent": 4}, safe=False)


def login_view(request):
    if request.method == "GET":
        return render(request, 'app/login.html')

    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            login(request, user)
            return redirect("app:user_profile")
        return render(request, "app/login.html", context={"error": "Неверные данные"})


def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


def register_view(request):
    if request.method == "GET":
        return render(request, 'app/register.html')

    if request.method == "POST":
        return render(request, 'app/register.html')


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("app:user_profile")
        return render(request, 'app/index.html')


def user_detail_view(request):
    if request.method == "GET":
        return render(request, 'app/user_details.html')

def get_text_json(request):
    if request.method == "GET":
        return JsonResponse({"text": get_random_text()},
                            json_dumps_params={"ensure_ascii": False})

