import sublime, sublime_plugin, ctypes

class DumpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#TODO: Remove dump()
		import pprint
		import struct
		def dump(obj):
			for attr in dir(obj):
				if hasattr(obj, attr):
					pprint.pprint((attr, getattr(obj, attr)), indent=2)
					print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

		dump(self.view)
		ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)
