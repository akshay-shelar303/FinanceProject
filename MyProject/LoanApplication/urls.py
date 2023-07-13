from django.urls import path
from .views import (
    home_view,
    create_sanctionedoan_view,
    show_sanctionedoan_view,
    update_sanctionedoan_view,
)

urlpatterns = [
    # path('', home_view, name='homepage'),
    path("create", create_sanctionedoan_view, name="create"),
    path("showsanctionloan", show_sanctionedoan_view, name="show_sanction"),
    path(
        "updatesanctionloan/<int:i>/", update_sanctionedoan_view, name="update_sanction"
    ),
]
