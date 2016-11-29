test = {
  'name': 'ttc_apply',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ttc_apply(lambda x: x*x, 7)
          49
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ttc_apply(lambda y: True, False)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ttc_apply(lambda x: x[0], [1, 2, 3])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ttc_apply(lambda y: 5, 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ttc_apply(lambda x: x[0](x[1]), [lambda x: x * x, 10])
          100
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from interpreter import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}