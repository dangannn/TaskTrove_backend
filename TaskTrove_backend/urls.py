"""
URL configuration for TaskTrove_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from info.views import news_list, add_news, delete_news, edit_news
from projects.views import ProjectsView, ProjectRequestsView
from ratings.views import CommentsView, FavoriteListsView
from users.views import UsersView, FreelancersView, CustomersView

router = SimpleRouter()
router.register('api/projects', ProjectsView)
router.register('api/users', UsersView)
router.register('api/freelancers', FreelancersView)
router.register('api/customers', CustomersView)
router.register('api/comments', CommentsView)
router.register('api/favorite_lists', FavoriteListsView)
router.register('api/requests', ProjectRequestsView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/news/', news_list, name='news_list'),
    path('api/add_news/', add_news, name='add_news'),
    path('api/news/<int:news_id>/delete/', delete_news, name='delete_news'),
    path('api/news/edit/<int:news_id>/', edit_news, name='edit_news'),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += router.urls
