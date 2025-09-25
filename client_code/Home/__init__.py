from ._anvil_designer import HomeTemplate
from anvil import *
import datetime

class Home(HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    current_hour = datetime.datetime.now().hour
    if current_hour < 5:
      self.title_label.text = "Sleep."
    elif current_hour < 12:
      self.title_label.text = "Good morning!"
    elif current_hour < 18:
      self.title_label.text = "Good afternoon."
    else:
      self.title_label.text = "Good night."
    
  def button_1_click(self, **event_args):
    open_form('Home')

  def button_2_click(self, **event_args):
    open_form('Timetable')
  
  def button_3_click(self, **event_args):
    open_form('Subject')

  def button_4_click(self, **event_args):
    open_form('Account')
