import wx
import myGUI

app = wx.App(False)
frame = myGUI.MainWindow()
# determin the user based on the currently logged in Windows User.
frame.InitMain()
frame.Show()
app.MainLoop()
