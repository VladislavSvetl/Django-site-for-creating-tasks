from .models import Task, Comment
from django.forms import ModelForm, widgets, TextInput, Textarea


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ["title", "task", "category"]
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название задачи'}),
            "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание задачи'}),
            "category": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите категорию задачи'})
        }


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ["username", "text"]
        widgets = {
            "username": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            "text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст комментария'})
        }
