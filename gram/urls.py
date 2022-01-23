from django.urls import path
from . import views
#swagger documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Mini Instagram Backend",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="Documented APIs"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('register/',views.Register.as_view(),name='register'),
    path('login/',views.TokenObtainPairView.as_view(),name='login'),
    path('create_album/',views.Create_Album,name='create_album'),
    path('publish_album/<int:id>/',views.Publish_Album,name='publish_album'),
    path('get_drafts/',views.GetALLDrafts,name='getting all drafts'),
    path('add_hashtags/<int:id>/',views.AddHashtags,name='adding_hashtags'),
    path('docs/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]  