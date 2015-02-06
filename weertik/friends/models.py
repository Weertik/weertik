from django.db import models
from django.contrib.auth.models import User


class friendship(models.Model):
    STATUS_LIST = ((u'W', u'Wait'),
                   (u'A', u'Accept'),
                   (u'B', u'Blocked'),
                   )
    from_user = models.ForeignKey(User,
                                  blank=False)
    to_user = models.ForeignKey(User,
                                blank=False)
    status = models.CharField('Status',
                              blank=False,
                              choizes=STATUS_LIST)
    date = models.DateTimeField(auto_now_add=True,
                                blank=True)
