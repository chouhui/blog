import time

from models import Model
from utils import formatted_time, log


class Blog(Model):
    @classmethod
    def valid_names(cls):
        names = super().valid_names()
        names = names + [
            'title',
            'content',
            'author',
            'created_time',
            'updated_time',
        ]
        return names

    @classmethod
    def new(cls, form, name):
        m = super().new(form)
        t = int(time.time())
        m.author = name
        m.created_time = t
        m.updated_time = t
        m.save()
        return m

    @classmethod
    def update(cls, id, form):
        m = super().update(id, form)
        log('blog update', m)
        m.updated_time = int(time.time())
        m.save()
        return m

    def formatted_created_time(self):
        return formatted_time(self.created_time)

    def formatted_updated_time(self):
        return formatted_time(self.updated_time)
