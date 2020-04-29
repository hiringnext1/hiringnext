from django.conf import settings
from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from .views import AdminDashboard, total_job_opening_list, total_resume_list, UserDashboard

urlpatterns = [
    url(r'^admin-dashboard/$', staff_member_required(AdminDashboard.as_view()), name='dashboard-admin'),
    url(r'^user-dashboard/$', UserDashboard.as_view(), name='dashboard-user'),

    url(r'^active-openings/$', total_job_opening_list, name='active_openings'),
    url(r'^active_resume/$', total_resume_list, name='active_resumes'),

]
