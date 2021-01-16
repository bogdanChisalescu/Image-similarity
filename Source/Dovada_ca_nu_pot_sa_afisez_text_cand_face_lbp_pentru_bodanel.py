import wx
import os

from interface_functions import *


########################################################################
class Panel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        #create chose img button
        btn_chose_img = wx.Button(self, label="Chose image", pos = (50, 50), size = (100, 30))
        btn_chose_img.Bind(wx.EVT_BUTTON, self.onButtonChoseImg)
        
        #info text
        self.text = wx.StaticText(self, label='Chose image from data set.', pos = (50, 30)) 

    #----------------------------------------------------------------------
    def onButtonChoseImg(self, event):
        """
        Change the value of self.call_function
        """
        #Get the image location
        openFileDialog.ShowModal()
        self.img_path = openFileDialog.GetPath()
        #openFileDialog.Destroy()
        
        #show chosen img
        chosen = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(self.img_path, wx.BITMAP_TYPE_ANY))
        chosen.SetPosition((450, 50))
        
        #create compute data set button
        btn_compute = wx.Button(self, label="Compute", pos = (50, 85), size = (100, 50))
        btn_compute.Bind(wx.EVT_BUTTON, self.onButtonCompute)
        
        #info text
        self.img_name = self.img_path.split("\\")[len(self.img_path.split("\\")) - 1]
        self.text.SetLabel("You selected the image " + self.img_name + "!") 
        
    
    #----------------------------------------------------------------------
    def onButtonCompute(self, event):
        
        #get images path (remove from img_path the name of the chosen image)
        print (self.img_path)
        data_set_path = self.img_path.replace("\\" + self.img_name,'')
        print (data_set_path)
        
        #list containing all the names of the images
        images = os.listdir(data_set_path)
        
        #lbp_img = compute_lbp_on_data_set(images, data_set_path)
        mask = np.array([[7,6,5], [0,0,4], [1,2,3]])
        mask = pow(2, mask)
    
        #execute lbp on every image in the dataset
        lbp_img = list()
        for i in range(len(images)):
            lbp_img.append(lbp(plt.imread(os.path.join(data_set_path, images[i])), 3, mask)) 
            self.text.SetLabel("Computing LBP for image no. " + str(i) )
            #lbp_img.append(mlbp(plt.imread(os.path.join(cwd, images[i])), 3, mask))
            #lbp_img.append(circular_lbp(plt.imread(os.path.join(cwd, images[i])), 3, 2))
        
        #info text
        self.text.SetLabel("Computing!") 
        
        
        
        
        #show the similar images
        similar1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(self.img_path, wx.BITMAP_TYPE_ANY))
        similar1.SetPosition((50, 330))
        
        similar2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(self.img_path, wx.BITMAP_TYPE_ANY))
        similar2.SetPosition((450, 330))
        
        similar3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(self.img_path, wx.BITMAP_TYPE_ANY))
        similar3.SetPosition((850, 330))

########################################################################
class Frame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="3 most similar images", size=(1300, 700))
        panel = Panel(self)
        panel.SetBackgroundColour("gray")
        self.Centre()
    
        
        self.Show()
        
   
        

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame()
    # Create open file dialog
    openFileDialog = wx.FileDialog(frame, "Open", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    
   

    app.MainLoop()
    