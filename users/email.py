from django.core.mail import send_mail

def send_confirm_email(email, code):
    send_mail(
        "Confirm your account",
        f"Your confirmation code: {code}",
        "noreply@gmail.com",
        [email],
        fail_silently=False,
    )