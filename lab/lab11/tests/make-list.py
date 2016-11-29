test = {
  'name': 'make-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> lst   ; type out exactly how Scheme would print the list
          ((1) 2 (3 . 4) 5)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab11)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}