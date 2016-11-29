test = {
  'name': 'ttc_eval',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'in_game_parse and end_game_parse',
          'choices': [
            'in_game_parse',
            'end_game_parse',
            'new_game',
            'in_game_parse and end_game_parse'
          ],
          'hidden': False,
          'locked': False,
          'question': 'ttc_eval takes in output from which function(s)?'
        },
        {
          'answer': 'ttc_apply',
          'choices': [
            'ttc_apply',
            'in_game_parse',
            'end_game_parse'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What function must be called in ttc_eval?'
        },
        {
          'answer': 'NewGame',
          'choices': [
            'Reset',
            'NewGame',
            'New'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which of the following is not a command a player can input?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> b = Board(False) # Create a board that doesn't print unnecessarily
          >>> line = "Place X at 7"
          >>> exp = in_game_parse(line)
          >>> ttc_eval(b, exp)
          'X has been placed in space 7'
          >>> ttc_eval(b, in_game_parse("O in for 6"))
          'O has been placed in space 6'
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