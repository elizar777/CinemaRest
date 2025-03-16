from rest_framework.routers import DefaultRouter

from apps.movies.views import MovieAPI

router = DefaultRouter()
router.register('movie', MovieAPI, 'api_moviews')

urlpatterns = router.urls