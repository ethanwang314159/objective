from ._anvil_designer import SubjectTemplate
from anvil import *


class Subject(SubjectTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

