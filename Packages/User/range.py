import sublime, sublime_plugin, re, math

class RangeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		reg = re.compile("[0-9]+( [0-9]*|)")

		for sel in sels:
			spl = self.view.substr(sel).split(" ")
			d1 = 1
			d2 = 0
			conc = ""

			d2 = int(spl[0])

			if len(spl) > 1:
				d1 = int(spl[1])

			if (d1 > d2):
				d1 = d1 + 1 if d1 > 0 else d1 - 1
				for i in range(d2, d1):
					conc += str(i) + "\n"
			else:
				d2 = d2 + 1 if d2 > 0 else d2 - 1
				for i in range(d1, d2):
					conc = str(i) + "\n" + conc

			self.view.replace(edit, sel, conc)