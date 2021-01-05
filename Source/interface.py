# First things, first. Import the wxPython package.
import wx


def onButtonFrm1(event): 
    frm1.Show() 

def onButtonFrm2(event): 
    print("merge") 


# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")
frm1 = wx.Frame(None, title="Fereastra 2")

panel = wx.Panel(frm, wx.ID_ANY) 
panel1 = wx.Panel(frm1, wx.ID_ANY) 


button = wx.Button(panel, wx.ID_ANY, 'Test', (10, 10)) 
button.Bind(wx.EVT_BUTTON, onButtonFrm1)  


button = wx.Button(panel1, wx.ID_ANY, 'Test', (10, 10)) 
button.Bind(wx.EVT_BUTTON, onButtonFrm2)
# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()  