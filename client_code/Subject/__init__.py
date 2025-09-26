from ._anvil_designer import SubjectTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Subject(SubjectTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    open_form('Home')

  def button_2_click(self, **event_args):
    open_form('Timetable')

  def button_3_click(self, **event_args):
    open_form('Subject')

  def button_4_click(self, **event_args):
    open_form('Account')

  def link_1_click(self, **event_args):
    open_form('Home')
