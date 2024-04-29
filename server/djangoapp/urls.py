from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'djangoapp'
urlpatterns = [
                  # path for registration
                  path(route='register', view=views.register_user, name='register'),

                  # path for login
                  path(route='login', view=views.login_user, name='login'),

                  # path for logout
                  path(route='logout', view=views.logout_user, name='logout'),

                  # path for get cars
                  path(route='get_cars', view=views.get_cars, name='get_cars'),

                  # path for get dealers
                  path(route='get_dealers', view=views.get_dealers, name='get_dealers'),

                  # path for get dealers by state
                  path(route='get_dealers/<str:state>', view=views.get_dealers, name='get_dealers_by_state'),

                  # path for get dealer by id
                  path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='get_dealer_details'),

                  # path for get dealer reviews
                  path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_reviews'),

                  # path for add a review view
                  path(route='add_review', view=views.add_review, name='add_review'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
