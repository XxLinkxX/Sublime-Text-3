import sublime, sublime_plugin, re, math

class GridMeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		reg = re.compile("[0-9]+ [0-9]+")
		for sel in sels:
			d1 = int(self.view.substr(sel).split(" ")[0])
			d2 = int(self.view.substr(sel).split(" ")[1])
			strbuilder = "[\r\n"
			for i in range(d1):
				st = "\t["
				for j in range(d2):
					st += "0, "
				strbuilder += st[:-2] + "],\r\n"
			self.view.replace(edit, sel, strbuilder[:-3] + "\r\n]\r\n")