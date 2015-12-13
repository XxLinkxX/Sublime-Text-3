import sublime, sublime_plugin

class ReadOnlyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if (self.view.is_read_only()):
			self.view.set_read_only(False)
		else:
			self.view.set_read_only(True)
