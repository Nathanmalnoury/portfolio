from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from contact.forms import MailForm


def contact(request):
    return render(request, 'contact.html')


def mail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MailForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            data = form.cleaned_data

            send_mail(
                "Django Website: '{}'".format(data["subject"]),
                'Message : \n\"{}\"\n-----\nName : \"{}\", eMail: \"{}\"'.format(data["text"], data["name"],
                                                                                 data["email"]),
                from_email=data["email"],
                recipient_list=['n.malnoury@gmail.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/contact/mail/')
        else:
            return render(request, 'contact.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MailForm()

    return render(request, 'mail.html', {'form': form})
