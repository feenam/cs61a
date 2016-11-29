test = {
  'name': '__contains__',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = Link(1, Link(2, Link(3)))
          >>> 2 in s
          True
          >>> 5 in s
          False
          >>> m = Link(5)
          >>> 1 in m
          False
          >>> 5 in m
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw08 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}