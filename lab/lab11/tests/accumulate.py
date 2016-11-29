test = {
  'name': 'accumulate',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (accumulate + 0 4 square)
          62f85fd6ec0a6a5c2930db3e7fc62c29
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (accumulate * 3 3 id)
          329324f549e9a87a0544b3661a9993b5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (accumulate + 1 5 add-one)
          6f3bafd4458acdc918b6576ef3c7fdaa
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab11_extra)
      scm> (define (square x) (* x x))
      scm> (define (id x) x)
      scm> (define (add-one x) (+ x 1))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}