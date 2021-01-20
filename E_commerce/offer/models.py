from oscar.apps.offer.models import *  # noqa isort:skip
from oscar.apps.offer.custom import create_condition
class Socio(Condition):
    name = "Preço Sócio"

    class Meta:
        proxy = True

    def is_satisfied(self, offer, basket):
        if not basket.owner:
            return False
        return basket.owner.Socio == True
create_condition(Socio)