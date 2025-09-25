from ._anvil_designer import SubjectTemplate
from anvil import *


class Subject(SubjectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_4_click(self, **event_args):
    target_url = "/Account"  # Replace with your desired URL
    anvil.js.window.open(target_url, "_self")
