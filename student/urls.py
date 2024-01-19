from django.urls import path

from student import views

urlpatterns = [
    path('dashboard/',views.StudentDashboard.as_view(),name='student_dashboard'),
    path('dashboard/<str:error>',views.StudentDashboard.as_view(),name='student_dashboard_error'),
    path('many/courses/',views.AllCourses.as_view(),name='many_course'),
    path('course/<slug:slug>/',views.SingleCourse.as_view(),name='enroll'),
    path('read/course/<slug:slug>/chapter/<int:pk>/<str:chapterName>/',views.ReadCourse.as_view(),name='read_course'),
    path('give/course/<slug:slug>/test/<int:pk>/<str:title>/',views.GiveTest.as_view(),name='give_test'),
    path('contact/',views.StudentContact.as_view(),name='student_contact'),
    path('many/course',views.StudentManyCourse.as_view(),name='student_many_course'),
]