import block
import logger
import pdb

""" Major design question: I chose to implement a one-way linked list for maintenance simplicity
over an easier to build harder to maintain two-way linked list (each block knows both the _next and _prev).
This choice has caused the implementation to be slower, because the disconnection process required tracking 
the parent of a block (if such exists) before transitioning it."""

class manager:
	""" The manager class which holds all blocks and transitions them as required """
	_blocks = []
	_logger = None

	def __init__(self, logger):
		if logger is None:
			self._logger = logger.logger()
		else:
			self._logger = logger

	def setSize(self, iPlaces):
		iPlaces = int(iPlaces)
		""" Initialize all block holders"""
		if type(iPlaces) != int:
			iPlaces = 10 #fallback

		self._logger.log(['setting manager size: ',iPlaces])
		for i in range(0,iPlaces):
			self._blocks.append(block.Block(i))

	###############################################
	# Basic transition functions

	def moveOnto(self, iA, iB):
		"""move a onto b. """
		if self._validateBlocks(iA, iB):
			self._blocks[iB].moveOnto(self._blocks[iA])

	def moveOver(self, iA, iB):
		"""move a over b"""
		if self._validateBlocks(iA, iB):
			self._blocks[iB].moveOver(self._blocks[iA])

	def pileOnto(self, iA, iB):
		"""pile a onto b"""
		if self._validateBlocks(iA, iB):
			self._blocks[iB].pileOnto(self._blocks[iA])

	def pileOver(self, iA, iB):
		"""pile a over b"""
		if self._validateBlocks(iA, iB):
			self._blocks[iB].pileOver(self._blocks[iA])

	###############################################

	def getParent(self, block):
		""" get the parent block of the given block. """
		if block.isAtHome(): return None #no container

		for i, parent in enumerate(self._blocks):
			container = parent.getParent(block)
			if container is not None:
				return container

		self._logger.logf("Problem! could not find container\n")
		return None #explicitely return None

	def printPiles(self):
		for i, block in enumerate(self._blocks):
			block.printPile(i)

	def report(self):
		"""used for debugging. prints to a log file"""
		for i, block in enumerate(self._blocks):
			self._logger.logf(block.reportPile(i) + '\n')
		self._logger.logf('\n**********************\n')

	###############################################
	# Private methods

	def _disconnectBeforeTransition(self, block):
		""" be sure to disconnect the block from its container (if such exists) before trnsitioning it"""
		blockContainer = self.getParent(block)
		if blockContainer is not None:
			blockContainer.disconnect()

	def _validateBlocks(self, iA, iB):
		a = self._blocks[iA]
		b = self._blocks[iB]
		valid = b is not None and a is not None \
				and not b.contains(a) and not a.contains(b)
		if valid:
			""" if the blocks are valid, be sure to disconnect block a before transitioning it to block b """
			self._disconnectBeforeTransition(a)
		return valid


