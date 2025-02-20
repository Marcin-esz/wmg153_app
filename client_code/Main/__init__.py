from ._anvil_designer import MainTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import State
from ..ExpenseDashboard import ExpenseDashboard
from ..Wykresy import Wykresy

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.switch_to_dashboard(None)
    if State.user['role'] == 'admin':
      self.separator_label_2.visible = True
      self.summary_btn.visible = True
      self.summary_btn.enabled = True

  def log_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('Login')

  def switch_to_dashboard(self, status):
    self.content_panel.clear()
    self.content_panel.add_component(ExpenseDashboard(status=status))
  
  def pendingappr_btn_click(self, **event_args):
    self.switch_to_dashboard('pending')

  def pendingreimb_btn_click(self, **event_args):
    self.switch_to_dashboard('approved')

  def pastexp_btn_click(self, **event_args):
    self.switch_to_dashboard(q.not_("pending", "approved"))

  def allexp_btn_click(self, **event_args):
    self.switch_to_dashboard(None)

  def summary_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Wykresy())

  def userLabel_show(self, **event_args):
    # Pobierz bieżącego użytkownika
    user = anvil.users.get_user()
    
    # Sprawdź, czy użytkownik jest zalogowany i posiada atrybut 'name'
    if user is not None and 'name' in user:
        # Przypisz nazwę użytkownika do etykiety
        self.userLabel.text = user['name']
    else:
        # Ustaw wartość domyślną, jeśli użytkownik nie jest zalogowany lub nie ma zdefiniowanej nazwy
        self.userLabel.text = " "

    


    
  














