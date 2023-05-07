import uuid
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm
from userextend.models import UserToken


# Create your views here.

class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save()

            get_token = uuid.uuid4().hex
            UserToken.objects.create(token=get_token, user_id=new_user.id, created_at=datetime.now())

            # trimiterea unui email FARA template
            # subject = 'Created a new account'
            # message = f'Congratulation, {new_user.first_name} {new_user.last_name}.'
            # send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            # Trimiterea unui email CU template
            # get_token_user = UserToken.objects.get(user_id=new_user.id).token
            # details_user = {
            #     'fullname': f'{new_user.first_name}, {new_user.last_name}',
            #     'username': new_user.username,
            #     'url': f'http://127.0.0.1:8000/activate_user/{new_user.id}/{get_token_user}/'
            # }
            #
            # subject = 'Created a new account'
            # message = get_template('mail.html').render(details_user)
            # mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
            # mail.content_subtype = 'html'
            # mail.send()


        return redirect('login')

def activate_user(request, pk, token):
    user_id = UserToken.objects.get(token=token, user_id=pk).user.id
    User.objects.filter(id=user_id).update(is_active=True)

    return redirect('login')
