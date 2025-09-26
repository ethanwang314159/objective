from ._anvil_designer import HomeTemplate
from anvil import *
from anvil.tables import app_tables
import datetime
from anvil import Label, ColumnPanel, GridPanel
import anvil

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
      anvil.server.reset_session()
      p_labels = [i['period'] for i in app_tables.monday.search()]
      p_times = [i['start_min'] for i in app_tables.monday.search()]
      print(p_labels)  # Log the records to check


      for k in range(len(p_labels)):
        new_label = Label(text=p_labels[k],
                          role="headline",
                          #font_size=20
                         )
        time_label = Label(text=p_times[k],
                          role="headline",
                          #font_size=20
                          )
        self.grid_panel_1.add_component(new_label)
        self.grid_panel_1.add_component(time_label, row=k)
      
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
