# tornwrap [![Build Status](https://api.travis-ci.org/stevepeak/tornwrap.svg?branch=master)](http://travis-ci.org/stevepeak/tornwrap) [![codecov.io](https://codecov.io/github/stevepeak/tornwrap/coverage.svg?branch=master)](https://codecov.io/github/stevepeak/tornwrap)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fcodecov%2Ftornwrap.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fcodecov%2Ftornwrap?ref=badge_shield)

> Collection of commonly used methods and decorators. Feedback and PRs welcome!

```sh
pip install tornwrap
```

## Project Contents

- [`@ratelimited`](#ratelimited)
  - limit usage for guests and authenticated users
- [`@validated`](#validated)
  - using [valideer](https://github.com/podio/valideer) to validate and adapt body and/or url args
- *future* [`@cached`](#cached)
  - cache requests, ex page builds
- *future* [`@gist`](#gist)
  - retrieve contents of a [gist](https://gist.github.com/) and return it to the handler
- *future* [`@markdown`](#markdown)
  - generate html pages from a Github repo containing markdown


# `@ratelimited`
> Requires `redis`

```python
from tornwrap import ratelimited

class Handler(RequestHandler):
    def initialize(self, redis):
        self.redis = redis # required

    @ratelimited(guest=(1000, 3600), user=(10000, 1800))
    def get(self):
        # users get 10k requests every 30 min
        # guests get 1k every 1h
        self.write("Hello, world!")

    def was_rate_limited(self, tokens, remaining, ttl):
        # this is the default action
        raise HTTPError(403, reason="You have been rate limited.")
```

# `@validated`
> Uses [valideer](https://github.com/podio/valideer)

```python
from tornwrap import validated

class Handler(RequestHandler):
    @validated({"+name":"string"})
    def get(self, arguments):
        # can validate url arguments
        self.finish("Hello, %s!" % arguments['name'])

    @validated(body={"+name":"string"})
    def post(self, body):
        # can validate body (json or urlencoded)
        self.finish("Hello, %s!" % body['name'])

```


# `@cached` (future feature)
> Cache the results of the http request.

```python
from tornwrap import cached

class Handler(RequestHandler):
    @cached(key="%(arg)s")
    def get(self, arg):
        # maybe a long api request
        return results # will call `self.finish(results)` for you

    def set_cache(self, key, data):
        self.memecached.set(key, data)

    def get_cache(self, key):
        return self.memecached.get(key)

```
> Will create methods for `async` methods to `get` and `set` too. We all <3 async!

# `@gist` (future feature)
> Fetch a Github gist content and return it to the handler method.
> Useful for chaning home page on the fly.

```python
from tornwrap import gist

class Handler(RequestHandler):
    @gist("stevepeak/5592167", refresh=False)
    def get(self, gist):
        self.render("template.html", gist=gist)
```
> `refresh` can be: `True`: fetch on every request, `False`: fetch right away, cache forever, `:seconds` till expires then refetch
> For those using Heroku, keep in mind dynos reset every 24 hours-ish.

# `@markdown` (future feature)
> Merge [torndown](https://github.com/stevepeak/torndown) project


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fcodecov%2Ftornwrap.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fcodecov%2Ftornwrap?ref=badge_large)