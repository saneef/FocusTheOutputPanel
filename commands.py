import sublime
import sublime_plugin

'''
  Focus the find results panel
'''

class FocusTheFindResultsPanelCommand(sublime_plugin.WindowCommand):
  def run(self):
    # Comment this line if the only have to focus if the panel is visible
    self.window.run_command('show_panel', args={'panel': 'output.find_results'})
    self.window.focus_view(self.window.find_output_panel('find_results'))
