from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ReviewValidator:

    def __call__(self, value):
        if value < 1 or value > 5:
            raise ValidationError(
                _("Введите значение от 1 до 5"),
                params={'value': value}
            )

    def deconstruct(self):
        return ('book.validators.ReviewValidator', [], {})