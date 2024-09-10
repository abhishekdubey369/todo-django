from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from .models import Todo
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
import json

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')

@method_decorator(csrf_exempt, name='dispatch')

class TodoCreateView(View):
    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if not title or not description:
            return HttpResponseBadRequest("Title and description are required.")
        
        Todo.objects.create(title=title, description=description)
        return redirect('todos:index')


class TodoUpdateView(View):
    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, pk=todo_id)
        
        # Handle the DELETE operation
        if request.POST.get('_method') == 'DELETE':
            todo.delete()
            return redirect('todos:index')

        # For updating the todo (if not a delete request)
        title = request.POST.get('title')
        description = request.POST.get('description')
        isCompleted = request.POST.get('isCompleted', False)

        if not title or not description:
            return HttpResponseBadRequest("Title and description are required.")
        
        todo.title = title
        todo.description = description
        todo.isCompleted = isCompleted == 'on'
        todo.save()

        return redirect('todos:index')




# class TodoView(View):
#     def post(self, request):
#         title = request.POST.get('title')
#         description = request.POST.get('description')
        
#         # Check if title and description are present
#         if not title or not description:
#             return HttpResponseBadRequest("Title and description are required.")
        
#         # Create new todo
#         Todo.objects.create(title=title, description=description)
        
#         # Redirect back to the todo list page after adding
#         return redirect('todos:index')

#     def put(self, request, todo_id):
#         # This part handles updating a todo, ensuring it's a valid request
#         todo = get_object_or_404(Todo, pk=todo_id)
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         isCompleted = request.POST.get('isCompleted', False)

#         if not title or not description:
#             return HttpResponseBadRequest("Title and description are required.")
        
#         todo.title = title
#         todo.description = description
#         todo.isCompleted = isCompleted == 'on'
#         todo.save()

#         return redirect('todos:index')

#     def delete(self, request, todo_id):
#         todo = get_object_or_404(Todo, pk=todo_id)
#         todo.delete()
#         return redirect('todos:index')


# class TodoView(View):
#     def get(self, request, todo_id=None):
#         if todo_id:
#             todo = get_object_or_404(Todo, pk=todo_id)
#             return JsonResponse({'id': todo.id, 'title': todo.title, 'description': todo.description, 'isCompleted': todo.isCompleted})
#         else:
#             todos = Todo.objects.all().values('id', 'title', 'description', 'isCompleted')
#             return JsonResponse(list(todos), safe=False)

#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             title = data.get('title')
#             description = data.get('description')
#             if not title or not description:
#                 return HttpResponseBadRequest("Title and description are required.")
#             if not isinstance(title, str) or not isinstance(description, str):
#                 return HttpResponseBadRequest("Title and description must be strings.")
            
#             Todo.objects.create(title=title, description=description)
#             return JsonResponse({'message': 'Todo created successfully'}, status=201)
#         except json.JSONDecodeError:
#             return HttpResponseBadRequest("Invalid JSON")

#     def put(self, request, todo_id):
#         try:
#             data = json.loads(request.body)
#             todo = get_object_or_404(Todo, pk=todo_id)
#             title = data.get('title')
#             description = data.get('description')
#             isCompleted = data.get('isCompleted', False)
            
#             if not title or not description:
#                 return HttpResponseBadRequest("Title and description are required.")
#             if not isinstance(title, str) or not isinstance(description, str):
#                 return HttpResponseBadRequest("Title and description must be strings.")
#             if not isinstance(isCompleted, bool):
#                 return HttpResponseBadRequest("isCompleted must be a boolean.")
            
#             todo.title = title
#             todo.description = description
#             todo.isCompleted = isCompleted
#             todo.save()
            
#             return JsonResponse({'message': 'Todo updated successfully'})
#         except json.JSONDecodeError:
#             return HttpResponseBadRequest("Invalid JSON")

#     def delete(self, request, todo_id):
#         todo = get_object_or_404(Todo, pk=todo_id)
#         todo.delete()
#         return JsonResponse({'message': 'Todo deleted successfully'})
