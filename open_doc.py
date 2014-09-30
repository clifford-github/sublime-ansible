import sublime, sublime_plugin
import webbrowser

class OpenDocCommand(sublime_plugin.TextCommand):

  def run(self, edit=None, url=None):

    if url is None:
      url = self.selection()

      url = "http://docs.ansible.com/" + url.replace(':', '') + "_module.html"
      webbrowser.open_new_tab(url)

  # pulls the current selection or url under the cursor
  def selection(self):
    s = self.view.sel()[0]

    # expand selection to possible URL
    start = s.a
    end = s.b

    # if nothing is selected, expand selection to nearest terminators
    if (start == end): 
      view_size = self.view.size()
      terminator = list('\t\"\'><, []()')

      # move the selection back to the start of the url
      while (start > 0
          and not self.view.substr(start - 1) in terminator
          and self.view.classify(start) & sublime.CLASS_LINE_START == 0):
        start -= 1

      # move end of selection forward to the end of the url
      while (end < view_size
          and not self.view.substr(end) in terminator
          and self.view.classify(end) & sublime.CLASS_LINE_END == 0):
        end += 1

    # grab the URL
    return self.view.substr(sublime.Region(start, end)).strip()

