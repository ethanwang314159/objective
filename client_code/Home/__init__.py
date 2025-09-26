from ._anvil_designer import HomeTemplate
from anvil import *
from anvil.tables import app_tables
from datetime import datetime
from anvil import Label, ColumnPanel, GridPanel
import anvil

class Home(HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    current_hour = datetime.now().hour
    if current_hour < 5:
      self.title_label.text = "Sleep."
    elif current_hour < 12:
      self.title_label.text = "Good morning!"
    elif current_hour < 18:
      self.title_label.text = "Good afternoon."
    else:
      self.title_label.text = "Good night."
    self.updateTimes()
    current_day_of_week = datetime.now().weekday()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    self.label_1.text = days_of_week[current_day_of_week]
    


  def updateTimes(self):
    try:
      # Fetch only a limited number of records (e.g., first 10)
      anvil.server.reset_session()
      p_labels = [i['period'] for i in app_tables.monday.search()]
      p_times = [i['start_min'] for i in app_tables.monday.search()]

      for k in range(len(p_labels)):
        new_label = Label(text=p_labels[k],
                          role="headline",
                          font_size=25
                         )
        self.grid_panel_1.add_component(new_label)

      for j in range(len(p_times)):
        ptime = p_times[j]
        readable_hr = str(ptime // 60).rjust(2, '0')
        readable_min = str(ptime % 60).rjust(2, '0')
        readable_time = "{}:{}".format(readable_hr, readable_min)
        time_label = Label(text=readable_time,
                           role="headline",
                           font_size=25
                          )

        now = datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        time_since_midnight = now - midnight
        minutes_since_midnight = int(time_since_midnight.total_seconds()) // 60
        diff_minutes = ptime - minutes_since_midnight
        if diff_minutes > 0:
          readable_diff_hour = str(diff_minutes // 60)#.rjust(2, '0')
          readable_diff_sec = str(diff_minutes % 60)#.rjust(2, '0')
          readable_diff = "{}h {}min until start".format(readable_diff_hour, readable_diff_sec)
          readable_diff_label = Label(text=readable_diff,
                                      role="headline",
                                      font_size=25
                                     )
        else:
          #print(ptime)
          #print(minutes_since_midnight)
          readable_diff_label = Label(text="Completed",
                                      role="headline",
                                      font_size=25)

        self.grid_panel_2.add_component(time_label)
        self.grid_panel_3.add_component(readable_diff_label)

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

  def link_1_click(self, **event_args):
    open_form('Home')

  def timer_1_tick(self, **event_args):
    self.updateTimes()