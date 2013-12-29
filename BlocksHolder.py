class BlocksHolder:
	_position = 0
	_blocks = []

	def __init__(self, position, block):
		"""Initialize a block holder."""
		_position = position
		_blocks[0] = block


	def pileBlock(self, block):
		"""Add blocks above current blocks"""
		if block is not None and type(block) == Block
			_blocks.append(block)

	def moveBlock(self, block):
		"""Clear all blocks and put a new one"""
		if block is not None and type(block) == Block
			_blocks = []
			self.pileBlock(block)

	def getBlocks():
		return _blocks

	def hasBlock(block):
		return block in _blocks
