from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .forms import LandingForm


class LandingView(View):
    def get(self, request):
        return render(request, 'landing/index.html')


    def post(self, request):
        received_data = request.POST

        form = LandingForm(received_data)
        if form.is_valid():
            ebook_form_name = form.cleaned_data.get("ebook_form_name")
            ebook_email = form.cleaned_data.get("ebook_email")
            # Заголовок HTTP_X_FORWARDED_FOR используется для идентификации исходного IP-адреса клиента,
            # который подключается к веб-серверу через HTTP-прокси или балансировщик нагрузки.
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')

            return JsonResponse({"name": ebook_form_name, "email": ebook_email, "ip": ip, "user_agent": user_agent},
                                json_dumps_params={"ensure_ascii": False, "indent": 4})

        return render(request, 'landing/index.html', context={"form": form})
