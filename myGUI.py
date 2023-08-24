import wx
import apiCalls
import dataset
from datetime import datetime

helptxt = f'Funktionen: \n Überprüfen - Ermittelt ob sich der Erkannte Benutzer in der Zentrale befindet \n Einchecken - Der erkannte Benuzer tritt dem Team Zentrale bei \n Auschecken - Der erkannte Benutzer verlässt die Zentrale unter der Bedingung das noch genug Mitarbeiter in der Zentrale sind. \n Mitgleider - Listet die akutellen Mitglieder in der Zentrale auf'


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        flexSizer = wx.FlexGridSizer(4,2,10,10)
        buttomSizer = wx.BoxSizer(wx.VERTICAL)

        #Currently Detected User
        currentDesc = wx.StaticText(self,label = "Erkannter Benutzer")
        self.recognizedUser = wx.TextCtrl(self, size = (400,22), style = wx.TE_READONLY)

        #Eventlogger
        self.logger = wx.TextCtrl(self,size = (400,300), style = wx.TE_MULTILINE | wx.TE_READONLY)

        #Buttoms
        self.ButtomCheck = wx.Button(self, label = "Überprüfen")
        self.ButtomIn = wx.Button(self, label = "Einchecken")
        self.ButtomOut = wx.Button(self, label =  "Auschecken")
        self.ButtomMember = wx.Button(self, label = "Mitglieder")

        self.Bind(wx.EVT_BUTTON, self.OnCheck, self.ButtomCheck)
        self.Bind(wx.EVT_BUTTON, self.OnIn, self.ButtomIn)
        self.Bind(wx.EVT_BUTTON, self.OnOut, self.ButtomOut)
        self.Bind(wx.EVT_BUTTON, self.OnMember, self.ButtomMember)

        #Grid Layout
        buttomSizer.AddMany([(self.ButtomCheck),(self.ButtomIn),(self.ButtomOut),(self.ButtomMember)])
        flexSizer.AddMany([(currentDesc),(self.recognizedUser),(buttomSizer),(self.logger)])
        flexSizer.AddGrowableCol(1,1)
        flexSizer.AddGrowableRow(2,1)
        mainSizer.Add(flexSizer, proportion = 2, flag = wx.ALL | wx.EXPAND, border = 15)
        self.SetSizer(mainSizer)


    #Funtctions
    def OnCheck(self, e):
        self.logger.AppendText(f'{datetime.now().strftime("%H:%M:%S")} - {str(apiCalls.teamCheck(apiCalls.currentUser))}\n')
        return
    
    def OnIn(self, e):
        self.logger.AppendText(f'{datetime.now().strftime("%H:%M:%S")} - {str(apiCalls.addToTeam(apiCalls.currentUser))}\n')
        return
    
    def OnOut(self, e):
        self.logger.AppendText(f'{datetime.now().strftime("%H:%M:%S")} - {str(apiCalls.complexeDelete(apiCalls.currentUser))}\n')
        return
    
    def OnMember(self,e):
        data = apiCalls.listMembers()
        if isinstance(data, list):
            self.logger.AppendText(f'{datetime.now().strftime("%H:%M:%S")} - Die {len(data)} Mitglieder sind: \n')
            for x in data:
                self.logger.AppendText(f'{x} \n')
        else:
            self.logger.AppendText(f'{datetime.now().strftime("%H:%M:%S")} - {data}')


    def Init(self):
        self.recognizedUser.AppendText(f'{apiCalls.currentUser} - {dataset.getDep(apiCalls.currentUser)}')
        if dataset.getDep(apiCalls.currentUser) == "unknown user":
            self.ButtomCheck.Disable()
            self.ButtomIn.Disable()
            self.ButtomOut.Disable()
            self.ButtomMember.Disable()
            self.logger.AppendText(f'{datetime.now().strftime("%H:%M:%S")} - {apiCalls.currentUser} hat keine Berechtigungen das Programm zu verwenden.')

            

            

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent = None, title = "Zentrale - Rein & Raus", size=(560,500))

        self.panel = MainPanel(self)
        
        #Statusbar
        self.CreateStatusBar()

        #Menu
        filemenu = wx.Menu()
        menuHelp = filemenu.Append(wx.ID_HELP, "Hilfe", "Programmhilfe")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "Über", "Informationen über dieses Programm")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"Beenden","Schließt das Programm")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"Datei")
        
        
        self.SetMenuBar(menuBar)      
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnHelp, menuHelp)

    def OnExit(self,e):
        self.Close(True) #close the Frame

    def OnAbout(self,e):
        dlg = wx.MessageDialog(self, f'geschrieben für B.E.S.T. Fluidsysteme GmbH München \n von Stephan Rott \n Version: v.4   -   24.08.2023' ,"Informationen über dieses Programm")
        dlg.ShowModal()
        dlg.Destroy()
    
    def OnHelp(self,e):
        dlg = wx.MessageDialog(self, helptxt,"Hilfe")
        dlg.ShowModal()
        dlg.Destroy()

    def InitMain(self):
        apiCalls.currentUser = apiCalls.initUser()
        MainPanel.Init(self.panel)
