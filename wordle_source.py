while (
	0 if 'attempts' in vars() else
		(attempts := 0)
		or ((u := True and "← CHANGE THIS IF YOU WANT DARK MODE COLORS") and not u)
		or ((v := False and "← CHANGE THIS IF YOU WANT HIGH CONTRAST MODE") and not v)
		or not (answers := list(map(str.strip, open('answers.txt').readlines())))
		or not (valids := list(map(str.strip, open('valid.txt').readlines())))
		or not (answer := __import__('random').choice(answers))
		or not (B := '\u001b[38;2;255;255;255;1;48;2;')
		or not (ABSENT := B+'58;58;60m')
		or not (PRESENT := B+'133;192;249m' if v else B+'181;159;59m' if u else B+'201;180;88m')
		or not (CORRECT := B+'245;121;48m' if v else B+'83;141;78m' if u else B+'106;170;100m')
		or not (ABSENT_EMOJI := chr(0x2b1b) if u else chr(0x2b1c))
		or not (PRESENT_EMOJI := chr(0x1f7e6) if v else chr(0x1f7e8))
		or not (CORRECT_EMOJI := chr(0x1f7e7) if v else chr(0x1f7e9))
		or not (LINEUP := '\u001b[F')
		or not (RESET := '\u001b[0m')
		or not (history := [[''] * 5 for _ in range(6)])

	) + 6 > attempts:

		print(
			LINEUP + f'{(attempts := attempts + 1)}. '
			+ ['', _answer := list(answer)][0].join(
				[
					CORRECT + i +
						['',
							history[attempts-1].__setitem__(idx, CORRECT_EMOJI),
							_answer.__setitem__(idx, '-')
						][0]
					if i == answer[idx]

					else
					PRESENT + i +
						['',
							history[attempts-1].__setitem__(idx, PRESENT_EMOJI),
							_answer.__setitem__(_idx, '-')
						][0]
					if (_idx := ([ 
							i == j and _in[jdx] != j
						for jdx, j in enumerate(_answer)] + [True]
					).index(True)) != 5

					else ABSENT + i +
						['',
							history[attempts-1].__setitem__(idx, ABSENT_EMOJI)
						][0]

				for idx, i in enumerate(list(_in))]) + RESET + ' ' * 20 + '\n'

				if (_in:=input(RESET+'\r> ')) in (valids + answers)
				else '\u001b[F' * 1 + ' ' * 20,

			end=["Genius","Magnificent","Impressive","Splendid","Great","Phew"][(attempts + (attempts:=6) - 7)] + '\n' + '\n'.join(map(''.join, history)) + '\nMicrordle\ngh:rfblock/wordle\n'
			if _in == answer
			else f'\nThe word was {answer}\n' + '\n'.join(map(''.join, history)) + '\nMicrordle\ngh:rfblock/wordle\n'
			if attempts == 6
			else ''
		)