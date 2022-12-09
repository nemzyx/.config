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

source_code = """#include <cstdio>
#include <iostream>
#include <string>
$user_includes
using namespace std;

int main()
{$user_commands
  return 0;
}
"""


def get_full_source( runner ):
	user_includes = list(runner.get_user_includes())
	user_commands = list(runner.get_user_commands())
	includes_replacement ='\n'  + runner.get_user_includes_string()
	commands_replacement ='\n  '+ runner.get_user_commands_string('  ')
	if len(user_includes) <= 0: includes_replacement = ''
	if len(user_commands) <= 0: commands_replacement = ''
	return ( source_code
		.replace( "$user_includes", includes_replacement )
		.replace( "$user_commands", commands_replacement )
		)

