from django import forms

from todo_list_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        max_length=400,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your task",
            }
        )
    )
    deadline = forms.DateTimeField(
        widget=forms.SelectDateWidget,
        required=False,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
