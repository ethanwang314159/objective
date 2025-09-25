from ._anvil_designer import TimetableTemplate
from anvil import *
from routing import router


class Timetable(TimetableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
