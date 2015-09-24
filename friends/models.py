from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    STATUS_LIST = (('W', 'Wait'), ('A', 'Accept'), ('B', 'Blocked'))
    from_user = models.ForeignKey(User, blank=False, related_name='from_user')
    to_user = models.ForeignKey(User, blank=False, related_name='to_user')
    status = models.CharField(
        'Status', max_length=10, blank=False, choices=STATUS_LIST, default='W')
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return '%s' % self.id
