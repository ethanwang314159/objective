from ._anvil_designer import HomeTemplate
from anvil import *
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
    try:
      # Fetch only a limited number of records (e.g., first 10)
      records = app_tables.monday.search(limit=1)
      print(records)  # Log the records to check
    except Exception as e:
      print(f"Error retrieving records: {e}")

  def button_1_click(self, **event_args):
    open_form('Home')

  def button_2_click(self, **event_args):
    open_form('Timetable')
  
  def button_3_click(self, **event_args):
    open_form('Subject')

  def button_4_click(self, **event_args):
    open_form('Account')
