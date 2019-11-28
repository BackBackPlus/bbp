import json

class JsonFunc(object):
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def return_json(self, name=None):
        if name is not None:
            return json.dumps({**self._kwargs, 'name': name}).encode('utf-8')
        return json.dumps(self._kwargs).encode('utf-8')

    @classmethod
    def home(cls):
        cla = cls()
        return cla.return_json

    @classmethod
    def not_found(cls):
        cla = cls(error=True)
        return cla.return_json()

    def __repr__(self):
        return f'JsonFunc(**kwargs:{self._kwargs!r})'


if __name__ == '__main__':
    jj = JsonFunc(a=1)
    pp = JsonFunc.home()
    print(jj, pp)
