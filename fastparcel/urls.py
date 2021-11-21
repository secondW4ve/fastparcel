from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from core import views
from core.customer import views as customer_views
from core.courier import views as courier_views

customer_urlpatterns = [
  path('', customer_views.home, name='home'),
  path('profile/', customer_views.profile_page, name='profile'),
  path('payment_method/', customer_views.payment_method_page, name='payment_method'),
  path('create_job/', customer_views.create_job_page, name='create_job'),

  path('jobs/current/', customer_views.current_jobs_page, name="current_jobs"),
  path('jobs/archived/', customer_views.archived_jobs_page, name="archived_jobs"),
  path('jobs/<job_id>/', customer_views.job_page, name="job"),
]

courier_urlpatterns = [
  path('', courier_views.home, name='home'),
  path('jobs/available/', courier_views.available_jobs_page, name='available_jobs'),
]


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('social_django.urls', namespace='social')),

  path('', views.home),

  path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
  path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
  path('sign-up/', views.sign_up),

  path('customer/', include((customer_urlpatterns, 'customer'))),
  path('courier/', include((courier_urlpatterns, 'courier'))),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
