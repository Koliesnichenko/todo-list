from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo_list_app.forms import TaskForm, TagForm
from todo_list_app.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_list_app/home.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list_app:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list_app:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list_app:task-list")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todo_list_app/tags_list.html"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list_app/tags_form.html"
    success_url = reverse_lazy("todo_list_app:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo_list_app:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo_list_app/tags_confirm_delete.html"
    success_url = reverse_lazy("todo_list_app:tag-list")


class TaskCompleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = True
        task.save()
        return redirect("todo_list_app:task-list")


class TaskUndoView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = False
        task.save()
        return redirect("todo_list_app:task-list")
