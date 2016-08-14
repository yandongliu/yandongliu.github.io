---
layout: post
title:  "Write A Python Backend Service"
date:   2016-08-10 16:12:22 -0800
categories: python backend rest
---

# High level structure of a Python backend service
 - Web/RPC layer (handle external requests)
 - Service layer (heavy business logic)
 - Repository layer (sychnronization with storage)

# Backend Components:

 - Storage layer: SQL database, NoSql, Cloud, etc.
 - SqlAlchemy: ORM
 - Alembic: Database migration management
 - Schematics: define entites, model validation
 - Web framework: Flask, Tornado, etc. for handling http requests
 - Other RPC framework if necessary e.g. Thrift
 - Job Queue: Celery etc.
 - Logging: kafka, log analysis, etc.
 - Monitoring: Sentry, Graphite, etc
 - Testing framework

# A data-centric view of the flow:

 - Request arrives at the handler
 - Invoke service layer to for busines logic
 - Read from DB through Repository layer and convert to Schematics objects (mappers)
 - End result is passed back as JSON object

# Discussion:
 - Model might be redefined as you'll define both SqlAlchemy and Schematics models for the same entity. Seems redundant.

# Simple implementation
{% highlight python %}

# servie layer
class BookstoreService(object)
    @classmethod
    def add_book(cls, user_id, book_id):
        user = yield UserRepository.read(user_id)
        book = yield BookRepository.read(book_id)
        user.books.append(book)
        yield UserRepository.update(user)

# repository layer
class UserRepository(object):
    @classmethod
    def read(cls, user_id):
        UserTable = User.__table__
        query = UserTable.select().where(UserTable.c.user_id == user_id)
        rows = session.execute(query)
        if rows:
            entities = map(UserMapper.to_entity_from_obj, list(rows))
            return entities[0]
    @classmethod
    def update(cls, user):
        ...

class BookRepository(object):
    ...

# define Schematics model
class User(Model):
    user_id = IntType(required=True)
    book_id = IntType(required=True)

class Book(Model):
    id = IntType(required=True)
    title = StringType(required=True)

# define Schematics mapper
class UserMapper(EntityMapper):
    _entity = User

class BookMapper(EntityMapper):
    _entity = Book

# define handler
class BookstoreHandler(BaseHandler):
    @gen.coroutine
    def post(self):
        user_id = self.get_argument('user_id')
        book_id = self.get_argument('book_id')
        yield BookstoreService.add_book(user_id, book_id)
        self.render("success.html")

{% endhighlight %}

I have a running boiletplate app at [Github](https://github.com/yandongliu/tornado_application).
