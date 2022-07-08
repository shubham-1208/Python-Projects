import cx_Freeze

executables = [cx_Freeze.Executable("Roll Dice.py")]

cx_Freeze.setup(
	name = "Dice Simulation",
	options = {"build_exe": {"packages":["pygame"], "include_files":["die1.png", "die2.png", "die3.png", "die4.png", "die5.png", "die6.png"]}},
	executables = executables
	)