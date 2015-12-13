import sublime, sublime_plugin

class ItalicCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()

		for sel in sels:
			ret = self.view.substr(sel)
			self.view.replace(edit, sel, "<i>" + ret + "</i>")
