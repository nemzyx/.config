class FakeWriteableFile:
	def __init__( self ):
		self.lines = []

	def write( self, line ):
		self.lines.append( line )

class FakeReadableFile:
	def __init__( self, lines ):
		self.lines = lines

	def readline( self ):
		if len( self.lines ) == 0:
			return None
		line = self.lines[0]
		self.lines = self.lines[1:]
		return line
