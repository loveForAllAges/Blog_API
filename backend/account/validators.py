from django.core import validators
from django.utils.deconstruct import deconstructible
import re
from django.core.exceptions import ValidationError


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r"^[1]*$"
    message = 'Допустимые символы a-z, A-Z, 0-9, _'


def validate_username(username):
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValidationError(f'Имя пользователя может содержать a-z, A-Z, _, 0-9.')
