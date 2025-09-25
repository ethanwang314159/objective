from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime
from anvil import Label, ColumnPanel, GridPanel

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
    print('hi')
    p_labels = [r['period'] for r in app_tables.my_table.search()]
    print(p_labels)
    for p_label in p_labels:
      new_label = Label(text="p_label",
                        foreground="blue",
                        font_size=20)
      self.column_panel_1.add_component(new_label)
    
    
  def button_1_click(self, **event_args):
    open_form('Home')

  def button_2_click(self, **event_args):
    open_form('Timetable')
  
  def button_3_click(self, **event_args):
    open_form('Subject')

  def button_4_click(self, **event_args):
    open_form('Account')
