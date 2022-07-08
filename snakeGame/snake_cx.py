import cx_Freeze

executables = [cx_Freeze.Executable("snake_game.py")]

cx_Freeze.setup(
	name = "Snake Game",
	options = {"build_exe": {"packages":["pygame"], "include_files":["PoetsenOne-Regular.ttf", "crunch.wav", "apple.png", "body_bl.png", "body_br.png", "body_tl.png", "body_tr.png", "body_horizontal.png", "body_vertical.png", "head_down.png", "head_up.png", "head_left.png", "head_right.png", "tail_down.png", "tail_left.png", "tail_right.png", "tail_up.png"]}},
	executables = executables
	)