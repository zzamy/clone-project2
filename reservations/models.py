from django.db import models
from core import models as core_models


class Reservation(core_models.TimeStampedModel):
    """Reservation model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRM = "confirm"
    STATUS_CANCELD = "canceled"

    STATUS_CHOICE = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRM, "confirm"),
        (STATUS_CANCELD, "canceled"),
    )

    status = models.CharField(choices=STATUS_CHOICE, max_length=20, default="pending")
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
