from django.forms import (
    Form,
    CharField,
    TextInput,
    EmailField,
    EmailInput
)


class NewsletterForm(Form):
    email = EmailField(label='Email', widget=EmailInput(attrs={'id': 'email'}))


class CommentForm(Form):
    message = CharField(label='Message', widget=TextInput(attrs={'id': 'message'}))
    name = CharField(label='Name', widget=TextInput(attrs={'id': 'name'}))
    email = EmailField(label='email', widget=EmailInput(attrs={'id': 'email'}))
    subject = CharField(label='Subject', widget=TextInput(attrs={'id': 'subject'}))
