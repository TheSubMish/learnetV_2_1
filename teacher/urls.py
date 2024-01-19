from django.urls import path
from .views import TeacherDashboard,TeacherContact,TeacherManyCourse,ManyEditPage

urlpatterns = [
    path('dashboard/',TeacherDashboard.as_view(),name='teacher_dashboard'),
    path('dashboard/<str:error>',TeacherDashboard.as_view(),name='teacher_dashboard_error'),
    path('contact/',TeacherContact.as_view(),name='teacher_contact'),
    path('many/course/',TeacherManyCourse.as_view(),name='teacher_many_course'),
    path('edit/course/<slug:slug>',ManyEditPage.as_view(),name='edit_course')
]
