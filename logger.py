from datetime import datetime

class logger:
	def log(self, lines):
		slog = str(datetime.now()) + ": "
		if type(lines) == list:
			for line in lines:
				slog += self.log(str(line) + ' ')
		else:
			slog += str(lines)

		return slog

	def logp(self, lines):
		print(self.log(lines))

	def logf(self, lines):
		f = open('log.txt','a')
		f.write(self.log(lines))
		f.close()