from ._anvil_designer import AccountTemplate
from anvil import *


class Account(AccountTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
  
  def button_1_click(self, **event_args):
    print('home')
    open_form('Home')

  def button_2_click(self, **event_args):
    open_form('Timetable')

  def button_3_click(self, **event_args):
    open_form('Subject')

  def button_4_click(self, **event_args):
    open_form('Account')
