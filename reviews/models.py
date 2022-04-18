from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()

    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # 리뷰를 삭제하면 이글을 작성한 리뷰내 유저정보가 필드에서 삭제 되어야 함
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    # 리뷰를 삭제하면 이글에서 언급한 리뷰내 룸정보가 필드에서 삭제 되어야 함

    def __str__(self):
        return f"{self.review} - {self.room}"
