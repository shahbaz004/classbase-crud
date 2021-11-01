from django.shortcuts import HttpResponseRedirect, render
from .forms import StudentForm
from .models import Student
from django.views.generic.base import TemplateView, RedirectView, View


# Updated
class StudentView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StudentForm()
        stud = Student.objects.all()
        context = {'stu': stud, 'form': form}
        return context

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")


class delete_data(RedirectView):
    url = "/"

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Student.objects.get(pk=del_id).delete()
        return super(delete_data, self).get_redirect_url()


class update_data(View):
    def get(self, request, id):
        u = Student.objects.get(pk=id)
        form = StudentForm(instance=u)
        return render(request, 'update.html', {'form': form})

    def post(self, request, id):
        u = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")
