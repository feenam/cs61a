test = {
  'name': 'What would Scheme print?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (+ 3 5)
          403f02fd254a4c6524542453898124b4
          # locked
          scm> (- 10 4)
          71dc1c0558e41b2d6d30fd9795b4fb1f
          # locked
          scm> (* 7 6)
          afa373c99abc5a519735aa7466635f88
          # locked
          scm> (/ 28 2)
          2ac3553c8fa906a0ec29e6b3fe8cf4ea
          # locked
          scm> (+ 1 2 3 4)
          994cc386b9ac20ceafc06b188d1ee65b
          # locked
          scm> (/ 8 2 2)
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          scm> (quotient 29 5)
          9934e055a74f1f7f5fb94c0f9fd6402d
          # locked
          scm> (remainder 29 5)
          3cfd97a152be55d1a3486dbacb2bf637
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (= 1 3)      ; True or False?
          5cab3718504a1a0efe676cfe3e714ac2
          # locked
          scm> (> 1 3)
          5cab3718504a1a0efe676cfe3e714ac2
          # locked
          scm> (< 1 3)
          308968ce50a38a2957823e1439417bf2
          # locked
          scm> (<= -1 -1)
          308968ce50a38a2957823e1439417bf2
          # locked
          scm> (or True False)
          308968ce50a38a2957823e1439417bf2
          # locked
          scm> (and True True)
          308968ce50a38a2957823e1439417bf2
          # locked
          scm> (and True False (/ 1 0))     ; Short-circuiting
          5cab3718504a1a0efe676cfe3e714ac2
          # locked
          scm> (not True)
          5cab3718504a1a0efe676cfe3e714ac2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define x 3)      ; Defining variables
          5ce45267887fa5dae1771a9b64b54929
          # locked
          scm> x
          350815b30c2ebeb01da1870d87346e85
          # locked
          scm> (define y (+ x 4))
          847f7c178da2025ec82e39b01a424bfd
          # locked
          scm> y
          3f8f8f09d1f65fa9740c33b3c16d4731
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}