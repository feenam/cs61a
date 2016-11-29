test = {
  'name': 'num-leaves',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (num-leaves nil)
          4b569bf0e21d6369c5343767f1146f64
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (num-leaves test-tree)
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (num-leaves (right test-tree))
          94ce22b5936436a75abf185df37ba826
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (num-leaves (left test-tree))
          94ce22b5936436a75abf185df37ba826
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab11_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}