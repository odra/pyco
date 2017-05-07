import inspect

import kelo


def test_from_fn(hello_world_fn):
  fn = kelo.from_fn(hello_world_fn)
  assert fn() == 'hello world'


def test_from_code(hello_world_fn):
  fn = kelo.from_code(hello_world_fn.__code__)
  assert fn() == 'hello world'


def test_from_fn_defaults(complex_fn):
  fn = kelo.from_fn(complex_fn)
  assert fn('odra') == 'odra is 32 years old and lives in nowhere'


def test_from_code_defaults(complex_fn):
  spec = inspect.getargspec(complex_fn)
  fn = kelo.from_code(complex_fn.__code__, defaults=spec.defaults)
  assert fn('odra', country='anywhere') == 'odra is 32 years old and lives in anywhere'
