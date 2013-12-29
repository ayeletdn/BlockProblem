import pdb

COLON 			= ":"
EMPTY_STRING 	= ""
SINGLE_SPACE 	= " "

class Block():
	"""The basic block element."""
	_nextBlock = None #pointer to the next block in line
	_me = 0 #know your position
	_atHome = True # indicates if the block is not "at home" (its original position)

	def __init__(self,pos):
		self._me = pos

	###############################################
	# Basic transition functions

	def moveOnto(self, block):
		""" puts block a onto block b 
		Anything above self is returned to original position 
		Anything above block is returned to original position """
		self._clearAbove()
		self.moveOver(block)

	def moveOver(self, block):
		""" put the block directly above self. 
		Anything above self is returned to original position 
		Anything above block retains its position """
		block._clearAbove()
		if self._nextBlock is None:
			self._nextBlock = block
		else:
			self._nextBlock.moveOver(block)
		block._moved()

	def pileOnto(self, block):
		""" clear all items above the block, 
		retain items above self
		put block at the top of self stack """
		self._clearAbove()
		self.pileOver(block)

	def pileOver(self, block):
		""" put the block on the top of the stack """
		if self._nextBlock is None:
			self._nextBlock = block
		else:
			self._nextBlock.pileOver(block)
		block._moved()

	###############################################

	def contains(self, block):
		"""recursively check if block contains other block"""
		if  self._nextBlock is None:
			"""no decendants"""
			return False
		else:
			""" direct or indirect decendant"""
			return self._nextBlock == block or self._nextBlock.contains(block)

	def disconnect(self):
		""" remove reference to the _nextBlock"""
		self._nextBlock = None

	def getParent(self, block):
		""" get the immediate parent of block """
		if self._nextBlock == None: 
			return None
		elif self._nextBlock == block:
			return self
		else:
			return self._nextBlock.getParent(block)

	def isAtHome(self):
		return self._atHome

	def printPile(self, pos):
		""" get the report of the pile and print it to stdout """
		ln = self.reportPile(pos)
		print(ln)

	def reportPile(self, pos):
		""" report the state of the block (but only if the block is at its original position) """
		ln = str(self._me) + COLON 
		if self._atHome:
			ln += self._reportBlock()
		return ln

	###############################################
	# Private methods

	def _clearAbove(self):
		""" removes any items stacked above """
		if self._nextBlock is not None:
			self._nextBlock._clearAbove() #itterative clear
			self._nextBlock._reset() #put blocks back in place
		self.disconnect() #remove any reference to the next block

	def _moved(self):
		"""mark this block as "not at home" """
		self._atHome = False

	def _reportBlock(self):
		""" get a full report of the block and its decendants """
		ln = str(self._me)
		if self._nextBlock is None:
			return ln
		else:
			return ln + SINGLE_SPACE + self._nextBlock._reportBlock()
		
	def _reset(self):
		"""Return the block to it's original position. (clear list below)"""
		self.disconnect()
		self._atHome = True


