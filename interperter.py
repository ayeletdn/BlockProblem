import logger
import block
import manager
import fileinput
import re
import pdb

QUIT = "quit"
MOVE = "move"
PILE = "pile"
OVER = "over"
ONTO = "onto"

class interperter:
	""" The main class, which performs the interpertation of the commands and runs them """
	_manager = None
	_logger = None

	def __init__(self):
		"""Initialize the interperter"""
		self._logger = logger.logger()
		self._manager = manager.manager(self._logger)

	def run(self):
		#_commandLines = self.loadCommandsFromFile('sample-data.txt')
		_commandLines = self._loadCommands()
		commands = self._parseCommands(_commandLines)
		self._executeCommands(commands)
		self._manager.printPiles()
		self._manager.report()

	def _executeCommand(self, command):
		""" execute a single command """
		a = command['a']
		b = command['b']
		c = command['command']
		""" validate the parameters """
		if type(a) is int and type(b) is int and callable(c):
			c(a,b)
		else:
			self._logger.logf(["command parameter passed is not a valid command dictionary, [", command, "]\n"])

	def _executeCommands(self, commands):
		""" execute a list of commands """
		if type(commands) is not list: 
			self._logger.logf("commands parameter passed is not a list\n")
			return
		for command in commands:
			self._executeCommand(command)
			
	def _getFunction(self, transfer, action):
		""" returns the matching function in the block manager """
		if transfer == MOVE and action == ONTO: return self._manager.moveOnto
		elif transfer == MOVE and action == OVER: return self._manager.moveOver
		elif transfer == PILE and action == ONTO: return self._manager.pileOnto
		elif transfer == PILE and action == OVER: return self._manager.pileOver
		else: self._logger.logf("transfer %s and action %s do not match functions\n"%(transfer, action))

	def _loadCommands(self):
		"""load the commands one by one from command line"""
		lines = []
		# first line must be the number of blocks
		s = input('--> ')
		self._manager.setSize(s)
		while s != QUIT:
			s = input('--> ')
			lines.append(s.lower())

		lines.remove(QUIT)
		return lines

	def _loadCommandsFromFile(self, fname):
		"""load the commands from a file. Does not expect quit """
		lines = [line.strip() for line in open(fname)]
		l0 = lines[0]
		self._manager.setSize(l0)
		lines.remove(l0)
		return lines

	def _parseCommand (self, command):
		"""parse a single line from the command"""
		res = re.search('(move|pile) (\d+) (over|onto) (\d+)', command)
		if res is not None:
			f = self._getFunction(res.group(1), res.group(3))
			a = int(res.group(2))
			b = int(res.group(4))
			return {'command': f, 'a': a, 'b': b}
		else:
			self._logger.logf("command [%s] did not produce any regex match\n"%command)

	def _parseCommands(self, lines):
		""" itterate input lines and parse the commands to a list of commands and their input params"""
		commands = []
		for command in lines:
			p = self._parseCommand(command)
			commands.append(p)
		return commands


#execute application
_interperter = interperter()
_interperter.run()