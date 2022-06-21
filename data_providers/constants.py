

class ProviderApplicationTypes:
    FIXER = 'Fixer'
    MOCK = 'Mock Application'

    @classmethod
    def get_choices(cls):
        return [
            (cls.FIXER, cls.FIXER),
            (cls.MOCK, cls.MOCK)
        ]