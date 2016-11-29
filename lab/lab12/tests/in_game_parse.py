test = {
  'name': 'in_game_parse',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> in_game_parse('Reset the board, please')
          ['Reset']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> in_game_parse('Reset the board X 1')
          ['Reset']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> in_game_parse('Place X on 1')
          ['Place', ['X', 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> in_game_parse('I want O to be placed on 6')
          ['Place', ['O', 6]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> in_game_parse('Please put X on 8')
          ['Place', ['X', 8]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> in_game_parse('Would you put O on 2')
          ['Place', ['O', 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> in_game_parse('7 X 5')
          ['Place', ['X', 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> in_game_parse('X O 3')
          ['Place', ['X', 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> in_game_parse('O 4 3')
          ['Place', ['O', 4]]
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