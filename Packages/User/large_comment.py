import sublime, sublime_plugin

class LargeCommentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()

		for sel in sels:
			spl = self.view.substr(sel)
			alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "?", "/", "+"]
			alpha += ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
			mxCount = 147
			fileType = self.view.file_name().split(".")[len(self.view.file_name().split(".")) - 1]
			fileCond = fileType in ["js", "cs", "css"]
			line1 = line2 = line3 = line4 = line5 = ""

			if fileCond:
				line1 = "    /*~ "
				line2 = "   /~~~ "
				line3 = "  /~~~~ "
				line4 = " /~~~~~ "
				line5 = "/~~~~~~ "
			else:
				line1 = "    /~ "
				line2 = "   /~~ "
				line3 = "  /~~~ "
				line4 = " /~~~~ "
				line5 = "/~~~~~ "

			R1 = ["  *  ", "**** ", " *** ", "**** ", "*****", "*****", " *** ", "*   *", "*****", "*****", "**  *", "*    ", "*   *", "*   *", " *** ", "**** ", " *** ", "**** ", " ****", "*****", "*   *", "*   *", "*   *", "*   *", "*   *", "*****",  "   ", " *** ", "    *", "     "]
			R2 = [" * * ", "*   *", "*   *", "*   *", "*    ", "*    ", "*    ", "*   *", "  *  ", "   * ", " * * ", "*    ", "** **", "**  *", "*   *", "*   *", "*   *", "*   *", "*    ", "  *  ", "*   *", "*   *", "*   *", " * * ", " * * ", "   * ",  "   ", "*   *", "   * ", "  *  "]
			R3 = ["*****", "**** ", "*    ", "*   *", "***  ", "***  ", "* ***", "*****", "  *  ", "   * ", " **  ", "*    ", "* * *", "* * *", "*   *", "**** ", "*   *", "**** ", " *** ", "  *  ", "*   *", " * * ", "* * *", "  *  ", "  *  ", "  *  ",  "   ", "   * ", "  *  ", "*****"]
			R4 = ["*   *", "*   *", "*   *", "*   *", "*    ", "*    ", "*   *", "*   *", "  *  ", "*  * ", " * * ", "*    ", "*   *", "*  **", "*   *", "*    ", "*  **", "*   *", "    *", "  *  ", "*   *", " * * ", "** **", " * * ", " *   ", " *   ",  "   ", "     ", " *   ", "  *  "]
			R5 = ["*   *", "**** ", " *** ", "**** ", "*****", "*    ", " *** ", "*   *", "*****", " **  ", "**  *", "*****", "*   *", "*   *", " *** ", "*    ", " ****", "*   *", "**** ", "  *  ", " *** ", "  *  ", "*   *", "*   *", "*    ", "*****",  "   ", "  *  ", "*    ", "     "]

			R1 += [" *** ", " **  ", "**** ", "**** ", "  ** ", "*****", " *** ", "*****", " *** ", " *** "]
			R2 += ["*  **", "* *  ", "    *", "    *", " * * ", "*    ", "*    ", "    *", "*   *", "*   *"]
			R3 += ["* * *", "  *  ", " *** ", "  ** ", "*****", "**** ", "**** ", "   * ", " *** ", " ****"]
			R4 += ["**  *", "  *  ", "*    ", "    *", "   * ", "    *", "*   *", "  *  ", "*   *", "    *"]
			R5 += [" *** ", "*****", " ****", "**** ", "   * ", "**** ", " *** ", "  *  ", " *** ", "    *"]

			for i in str(spl):
				line1 += R1[alpha.index(i.lower())] + "   "
				line2 += R2[alpha.index(i.lower())] + "   "
				line3 += R3[alpha.index(i.lower())] + "   "
				line4 += R4[alpha.index(i.lower())] + "   "
				line5 += R5[alpha.index(i.lower())] + "   "

			line1 = line1[:-3] + "     "
			line2 = line2[:-3] + "    "
			line3 = line3[:-3] + "   "
			line4 = line4[:-3] + "  "
			line5 = line5[:-3] + " "

			line1 += "".join(["~" for x in range(len(spl))]) + "~~~~"
			line2 += "".join(["~" for x in range(len(spl))]) + "~~~~"
			line3 += "~ " + spl.title() + " ~"
			line4 += "".join(["~" for x in range(len(spl))]) + "~~~~"
			line5 += "".join(["~" for x in range(len(spl))]) + "~~~~"

			while (len(line1) < mxCount): line1+= "~"
			while (len(line2) < mxCount - 1): line2+= "~"
			while (len(line3) < mxCount - 2): line3+= "~"
			while (len(line4) < mxCount - 3): line4+= "~"
			while (len(line5) < mxCount - 4): line5+= "~"

			if fileCond:
				line1 += "~/"
				line2 += "~/"
				line3 += "~/"
				line4 += "~/"
				line5 += "*/"
			else:
				line1 = "<!--\n" + line1 + "/"
				line2 += "/"
				line3 += "/"
				line4 += "/"
				line5 += "/\n-->"

			ret = "\n".join([line1, line2, line3, line4, line5])

			self.view.replace(edit, sel, ret)