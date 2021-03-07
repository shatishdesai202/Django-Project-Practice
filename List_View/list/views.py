from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student


class StudentListView(ListView):
    model = Student
    template_name_suffix = "_desai"
    ordering = ['name']
    template_name = 'desai/abc.html'
    # get_queryset
    context_object_name = 'obj'
    # default  context_object_name = 'student_list'
    

    def get_queryset(self):
        # set session storage
        self.request.session['user'] = 'shatish'

        return Student.objects.filter(name="shatish")

    # another context variable
    def get_context_data(self, **kwargs):
        print(self.request.session['user'])
        context = super().get_context_data(**kwargs)

        context["custom_objects"] = Student.objects.all().order_by(
            '-roll_number')
        return context

    # template rendering
    def get_template_names(self):

        if self.request.session['user'] == 'shatish':
            template_name = 'list/student_desai.html'
        else:
            template_name = self.template_name

        return[template_name]
