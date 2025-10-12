from ._anvil_designer import HomeTemplate
from anvil import *
from anvil.tables import app_tables
from datetime import datetime

class Home(HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.storage = []

    hour = datetime.now().hour
    if hour < 5:
      self.title_label.text = "Sleep."
    elif hour < 12:
      self.title_label.text = "Good morning!"
    elif hour < 18:
      self.title_label.text = "Good afternoon."
    else:
      self.title_label.text = "Good night."

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    self.label_1.text = days[datetime.now().weekday()]

    records = list(app_tables.monday.search())
    self.p_labels = [r['period'] for r in records]
    self.p_times = [r['start_min'] for r in records]

    self.updateTimes()

  def updateTimes(self):
    try:
      self.grid_panel_1.clear()
      self.grid_panel_2.clear()
      self.grid_panel_3.clear()

      now = datetime.now()
      minutes_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).seconds // 60

      for period, start_min in zip(self.p_labels, self.p_times):
        self.grid_panel_1.add_component(Label(text=period, role="headline", font_size=25))

        start_str = f"{start_min//60:02d}:{start_min%60:02d}"
        self.grid_panel_2.add_component(Label(text=start_str, role="headline", font_size=25))

        diff = start_min - minutes_since_midnight
        if diff > 0:
          hours, mins = divmod(diff, 60)
          diff_text = (f"{hours}h " if hours else "") + (f"{mins}min" if mins else "")
        else:
          diff_text = "Completed"

        self.grid_panel_3.add_component(Label(text=diff_text, role="headline", font_size=25))

    except Exception as e:
      print(f"Error retrieving records: {e}")

  def button_1_click(self, **event_args): open_form('Home')
  def button_2_click(self, **event_args): open_form('Timetable')
  def button_3_click(self, **event_args): open_form('Subject')
  def button_4_click(self, **event_args): open_form('Account')
  def button_5_click(self, **event_args): open_form('About')
  def link_1_click(self, **event_args): open_form('Home')
  def timer_1_tick(self, **event_args): self.updateTimes()
