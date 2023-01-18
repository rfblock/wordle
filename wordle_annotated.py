while (                                                                                    # Everything runs inside this while loop
	0 if 'attempts' in vars() else                                                         # This is a ternary operater that with the
		(attempts := 0)                                                                    # condition that 'attempts' has not yet been defined
		or ((u := True and "← CHANGE THIS IF YOU WANT DARK MODE COLORS") and not u)        # It runs this chunk of code that declares everything
		or ((v := False and "← CHANGE THIS IF YOU WANT HIGH CONTRAST MODE") and not v)     # It uses the fact that `0 or False` == False
		or not (answers := list(map(str.strip, open('answers.txt').readlines())))          # So, everything after `(attempts := 0)` is designed to be falsy
		or not (valids := list(map(str.strip, open('valid.txt').readlines())))
		or not (answer := __import__('random').choice(answers))
		or not (B := '\u001b[38;2;255;255;255;1;48;2;') # White + Bold + FG[r,g,b]         # Some ANSI Formatting codes
		or not (ABSENT := B+'58;58;60m') #3a3a3c
		or not (PRESENT := B+'133;192;249m' if v else B+'181;159;59m' if u else B+'201;180;88m') #c9b458, #b59f3b, #85c0f9
		or not (CORRECT := B+'245;121;48m' if v else B+'83;141;78m' if u else B+'106;170;100m') #6aaa64, #538d4e #f5793a
		or not (ABSENT_EMOJI := chr(0x2b1b) if u else chr(0x2b1c))  # ⬛⬜
		or not (PRESENT_EMOJI := chr(0x1f7e6) if v else chr(0x1f7e8)) # 🟦🟨
		or not (CORRECT_EMOJI := chr(0x1f7e7) if v else chr(0x1f7e9)) # 🟧🟩
		or not (LINEUP := '\u001b[F')
		or not (RESET := '\u001b[0m')
		or not (history := [[''] * 5 for _ in range(6)])                                   # This is used for emojis
		# or not not print('\u001b[2J' + answer) # `not not ...` is effectively bool(...) # This is a debug statement, uncomment to get the word before every game
	) + 6 > attempts:

		print(                                                    # This is start of the main loop
			LINEUP + f'{(attempts := attempts + 1)}. '            # Extra statements can be squeezed into strings
			+ ['', _answer := list(answer)][0].join(              # By using `['', /statemnet/][0]`, as `statement`
				[                                                 # will be ran but only an empty string will be returned
					CORRECT + i +
						['',
							history[attempts-1].__setitem__(idx, CORRECT_EMOJI),    # `_answer` is used to match duplicates
							_answer.__setitem__(idx, '-')                           # When a match is found, it is removed from `_answer`
						][0]
					if i == answer[idx]                                             # `if` statements are created with nested ternary statements
                                                                                    # if condition1: statement1
					else                                                            # elif condition2: statement2
					PRESENT + i +                                                   # else: statement3
						['',                                                        # 
							history[attempts-1].__setitem__(idx, PRESENT_EMOJI),    # Is created by
							_answer.__setitem__(_answer.index(i), '-')              #
						][0]                                                        # statement1
					if i in _answer                                                 # if condition1
                                                                                    # 
					else ABSENT + i +                                               # else statement2
						['',                                                        # if condition2
							history[attempts-1].__setitem__(idx, ABSENT_EMOJI)      # 
						][0]                                                        # else condition3

				for idx, i in enumerate(list(_in))]) + RESET + ' ' * 20 + '\n' # The previous chunk of code is repeated for every character inputted
                                                                               # 20 spaces are added to the end to clear anything that would've been left over (hacky, oh well)
				if (_in:=input(RESET+'\r> ')) in (valids + answers)
				else '\u001b[F' * 1 + ' ' * 20,

			# The ending statement only shows the "game over" text when you run out of attempts or you guess the word
			# Word was guessed
			end=["Genius","Magnificent","Impressive","Splendid","Great","Phew"][(attempts + (attempts:=6) - 7)] + '\n' + '\n'.join(map(''.join, history)) + '\nMicrordle\ngh:rfblock/wordle\n'
			if _in == answer

			# Word was not guessed
			else f'\nThe word was {answer}\n' + '\n'.join(map(''.join, history)) + '\nMicrordle\ngh:rfblock/wordle\n'
			if attempts == 6

			# Default
			else ''
		)