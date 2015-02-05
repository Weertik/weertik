from .models import *
from datetime import date, timedelta
import kronos


@kronos.register('0 * * * *')
def _del_token():
    token_list = Token_auth.objects.filter(
        date__range=[(date.today()-timedelta(days=365)),
                     (date.today()-timedelta(days=1))])
    for token in token_list:
        token.delete()
