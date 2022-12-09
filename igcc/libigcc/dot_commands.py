# igcc - a read-eval-print loop for C/C++ programmers
#
# Copyright (C) 2009 Andy Balaam
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
import os
import source_code
import copying

import run
from fake import FakeReadableFile, FakeWriteableFile
def fake_eval(cmd, runner): # no write to full source code
	# only works for a single line of c
	commands = []
	for line in runner.get_user_includes():
		commands.append(line)
	for line in runner.get_user_commands():
		commands.append(line)
	commands.append(cmd)
	inputFile = FakeReadableFile( commands )
	outputfile = FakeWriteableFile()
	ret, fake_runner = run.run(outputfile, inputFile, False, None)
	if fake_runner.compile_error is not None: # transfer error to stdin
		runner.compile_error = fake_runner.compile_error
	possible_outs = outputfile.lines[-4:-2]
	possible_outs[-1] = possible_outs[-1][:-1]
	if possible_outs[1]: # success
		return possible_outs[1]
	else:
		return possible_outs[0]

class IGCCQuitException:
	pass

def dot_c( runner, args ):
	print copying.copying
	return False, False

def dot_e( runner, args ):
	if runner.compile_error:
		print runner.compile_error,
	return False, False

def dot_q( runner, args ):
	raise IGCCQuitException()

def dot_l( runner, args ):
	print ''
	user_includes_cnt = len(list(runner.get_user_includes()))
	user_commands_cnt = len(list(runner.get_user_commands()))
	if user_includes_cnt > 0:
		print runner.get_user_includes_string()
	if user_commands_cnt > 0:
		print runner.get_user_commands_string()
	if (user_commands_cnt+user_includes_cnt) <= 0:
		print '[No code yet]'
	return False, False

def dot_L( runner, args ):
	print ''
	print source_code.get_full_source( runner )
	return False, False

def dot_r( runner, args ):
	redone_line = runner.redo()
	if redone_line is not None:
		print "[Redone '%s'.]" % redone_line
		return False, True
	else:
		print "[Nothing to redo]"
		return False, False
		
def dot_u( runner, args ):
	undone_line = runner.undo()
	if undone_line is not None:
		print "[Undone '%s'.]" % undone_line
	else:
		print "[Nothing to undo]"
	return False, False

def dot_w( runner, args ):
	print copying.warranty
	return False, False

def dot( runner, args ): # cout << [var] << endl;
	if len(args) <= 0:
		print "Use the . command to inspect data"
		print "Shorthand for 'cout << [var] << endl;'"
		return False, False # early
	xpr = args
	cmd = 'cout << ' + xpr + ' << endl;'
	res = fake_eval(cmd, runner)
	print(res)
	return False, False

dot_commands = {
	"."  : (" Inspect data ( cout << [var] )", dot, 10 ),
	".e" : ( "Show the last compile errors/warnings", dot_e, 20 ),
	# ".h" : ( "Show this help message", None, 30 ),
	".l" : ( "List the code you have entered", dot_l, 40 ),
	".L" : ( "List full program (as given to compiler)", dot_L, 50 ),
	".u" : ( "Undo previous command", dot_u, 60 ),
	".r" : ( "Redo undone command", dot_r, 70 ),
	".q" : ( "Quit", dot_q, 80 ),
	# ".c" : ( "Show copying information", dot_c, 90 ),
	# ".w" : ( "Show warranty information", dot_w, 100 ),
	}

def clear():
	os.system('clear')
	run.print_welcome()
	return False, False

def dot_h():
	print ''
	for cmd in sorted(dot_commands.keys(), key=lambda x: dot_commands[x][2]):
		print '  ' + cmd, dot_commands[cmd][0]
	print ''
	return False, False

def process( inp, runner ):
	inp = inp.strip()
	if inp == "clear": return clear()
	if len(inp) <= 0 or inp[0] != '.': return True, True # early

	inp_arg = " ".join(inp.split(' ')[1:])
	inp_cmd =          inp.split(' ')[0]
	if inp_cmd == ".h":
		return dot_h()

	for cmd in dot_commands.keys():
		if inp_cmd == cmd:
			return dot_commands[cmd][1]( runner, inp_arg )

	return True, True
