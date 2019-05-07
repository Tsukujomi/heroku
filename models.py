from smartninja_nosql.odm import Model


class SecretNumbe(Model):
    def __init__(self, number, **kwargs):
        self.name = name
        self.secret_number = secret_number
        super().__init__(**kwargs)