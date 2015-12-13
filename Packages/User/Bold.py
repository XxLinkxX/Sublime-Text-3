import sublime, sublime_plugin

class BoldCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()

		for sel in sels:
			ret = self.view.substr(sel)
			self.view.replace(edit, sel, "<b>" + ret + "</b>")
