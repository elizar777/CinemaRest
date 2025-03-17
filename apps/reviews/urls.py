from rest_framework.routers import DefaultRouter

from apps.reviews.views import ReviewAPI 

router = DefaultRouter()
router.register('review', ReviewAPI, 'api_review')

urlpatterns = router.urls