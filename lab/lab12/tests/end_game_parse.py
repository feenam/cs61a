test = {
  'name': 'end_game_parse',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> end_game_parse("yes")
          ['New']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> end_game_parse("no")
          ['End']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> end_game_parse("I do not like this game.") # 'not' begins with 'n'
          ['End']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> end_game_parse("I could play against you all day") # 'you' begins with 'y'
          ['New']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> end_game_parse("Purple snacks never yaks")
          ['End']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> end_game_parse("There are zero valid commands in this line")
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