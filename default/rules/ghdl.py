from rules.base import SourceLocation, Target

SourceLocation(
	name = 'ghdl',
	vcs = 'git',
	location = 'https://github.com/ghdl/ghdl',
	revision = 'origin/master',
)

Target(
	name = 'ghdl',
	sources = [ 'ghdl' ],
	arch = [ 'linux-x64' ],
	license_file = 'ghdl/COPYING.md',
)
