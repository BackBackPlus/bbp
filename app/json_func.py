import json


class JsonFunc(object):
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def return_json(self) -> json:
        return json.dumps(self._kwargs)

    @classmethod
    def home(cls):
        return cls(learn_num=1,
                   all_num=100,
                   process=1 / 100).return_json

    @classmethod
    def not_found(cls):
        return cls(error=True).return_json()

    @classmethod
    def word_return(cls):
        return cls(word='',
                   ).return_json()

    @classmethod
    def sort_player(cls):
        return cls(id=0,
                   plyer_name='',
                   lw_num=0).return_json()

    def __repr__(self):
        return f'JsonFunc(**kwargs:{self._kwargs!r})'


if __name__ == '__main__':
    jj = JsonFunc(a=1)
    pp = JsonFunc.home()
    print(jj)
    print(pp)
