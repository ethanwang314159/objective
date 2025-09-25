from ._anvil_designer import SubjectTemplate
from anvil import *
from routing import router


class Subject(SubjectTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

