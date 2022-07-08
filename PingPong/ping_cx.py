import cx_Freeze

executables = [cx_Freeze.Executable("ping_pong.py")]

cx_Freeze.setup(
	name = "Ping Pong",
	options = {"build_exe": {"packages":["pygame"], "include_files":["PoetsenOne-Regular.ttf", "pong.ogg", "score.ogg"]}},
	executables = executables
	)