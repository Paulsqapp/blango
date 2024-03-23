
from django.urls import path, include, re_path
from blog.api.views import PostList, PostDetail, UserDetail, TagViewSet
from blog.api.views import UserDetail, TagViewSet, PostViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter


#swagger
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os

# DRF routers
#router = DefaultRouter()
#router.register("tags", TagViewSet)
#router.register("posts", PostViewSet)


urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    #path("", include(router.urls)),
    path("posts/by-time/<str:period_name>/",
        PostViewSet.as_view({"get": "list"}),
        name="posts-by-time",
    ),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    #re_path removed due to error
    
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)

