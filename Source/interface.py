# First things, first. Import the wxPython package.
import wx


def onButtonFrm1(event):
     openFileDialog.ShowModal()
     img_path = openFileDialog.GetPath()
     openFileDialog.Destroy()
     png = wx.Image(img_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
     wx.StaticBitmap(frm,-1, png, (100, 100), (png.GetWidth(), png.GetHeight()))
     

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")


panel = wx.Panel(frm, wx.ID_ANY) 


button = wx.Button(panel, wx.ID_ANY, 'Test', (10, 10)) 
button.Bind(wx.EVT_BUTTON, onButtonFrm1)  


button = wx.Button(panel, wx.ID_ANY, 'asdfasd', (70, 70)) 

# Create open file dialog
openFileDialog = wx.FileDialog(frm, "Open", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)


# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()  