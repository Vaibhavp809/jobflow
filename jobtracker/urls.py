
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jobtracker.jobs.views import JobViewSet
from jobtracker.jobs.views import dashboard, applications, add_job_page, analytics, about

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
urlpatterns = [
    path('admin/', admin.site.urls),

    # Web Pages
    path('', dashboard, name='dashboard'),
    path('applications/', applications, name='applications'),
    path('add/', add_job_page, name='add_job'),
    path('analytics/', analytics, name='analytics'),
    path('about/', about, name='about'),

    # API
    path('', include(router.urls)),
    path('jobs/status/<str:status>/', JobViewSet.as_view({'get': 'filter_by_status'})),
]