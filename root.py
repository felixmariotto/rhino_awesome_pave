"""
root file of rhino_awesome_pave.
Its only job is to make an instance of the main UI and add
it to Rhino window.
"""

from imp import reload

from ui import main
from ui import keymanager
from functions import handler


import Rhino
import scriptcontext as sc

reload(main)
reload(keymanager)
reload(handler)

main.Form.H = handler.Handler


# The form will be kept track of in the scriptcontext sticky under this key
MAIN_FORM_STICY = "awesome_pave_main_form"


# Whenever the form is closed, remove it from the scriptcontext sticky
def OnClosed(sender, args):
    if MAIN_FORM_STICY in sc.sticky:
        del sc.sticky[MAIN_FORM_STICY]


def rhino_awesome_pave():

    # Do nothing if the form is visible
    if MAIN_FORM_STICY in sc.sticky: return

    # Create a new form
    form = main.Form()
    form.Owner = Rhino.UI.RhinoEtoApp.MainWindow
    # Hook to the Closed event
    form.Closed += OnClosed
    form.Show()

    kpm = keymanager.KeyPressManager()
    kpm.addIncreaseCallback( form.handleIncrease )
    kpm.addDecreaseCallback( form.handleDecrease )

    # Keep the ref in the scriptcontext sticky
    sc.sticky[MAIN_FORM_STICY] = form


if __name__ == '__main__':
    rhino_awesome_pave()
    
