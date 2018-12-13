import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from jsonLoader import msf, weather
from teams import teamDict, teamCity, indoor
from msfCompatable import makeCompatable
from PIL import Image, ImageTk

class Feedback:

    def __init__(self, master):
        # weatherData = weather('KS', 'Overland_Park')
        # sportsData = msf('2018-2019-regular','full_game_schedule', 'KansasCity-Chiefs')
        teams = teamDict()

        master.title('A Foot in the Door')
        master.resizable(False, False)
        master.geometry('800x600')
        # master.configure(background = '#8D230F')
        self.style = ttk.Style()
        self.style.configure('TFrame', background = 'white')
        self.style.configure('TButton', background = 'white')
        self.style.configure('TLabel', background = '#DCDCDC', font = ('Arial', 14))
        self.style.configure('Header.TLabel', background = '#003366', foreground = 'white', font = ('Roboto', 36, 'bold'))
        self.style.configure('Header2.TLabel', background = '#DCDCDC', foreground = '#003366', font = ('Roboto', 30, 'bold'))
        
        self.bgfile = PhotoImage(file = 'E:/school/2018-19/caps/A Foot in the Door/images/szn7w.gif')
        self.transpic = PhotoImage(file = 'E:/school/2018-19/caps/A Foot in the Door/images/asfalt-light.gif')
        self.bglabel = Label(master, image = self.bgfile)
        self.bglabel.place(x=0, y=0, relwidth=1, relheight=1)

        
        # self.image = tk.PhotoImage(file='E:/school/2018-19/caps/A Foot in the Door/images/asfalt-light.gif')
        # self.label = tk.Label(master, image= self.image, bg='white')
        # master.overrideredirect(True)
        # master.lift()
        # master.wm_attributes("-topmost", True)
        # master.wm_attributes("-disabled", True)
        # master.wm_attributes("-transparentcolor", "white")
        # self.label.pack()
        # self.label.mainloop()
        

        self.title_page = ttk.Frame(master)
        self.title_page.pack()
        # , image = self.transpic
        self.bglabel = Label(self.title_page)
        self.bglabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.header = ttk.Label(self.title_page, text = 'Weather \'n Football!',
                            style = 'Header.TLabel').pack()
        
        tkvar = StringVar(master)
        tkvar.set('Select Team')

        self.menu = OptionMenu(self.title_page, tkvar, *teams, command = self.startSearch)
        self.menu['highlightthickness'] = 0
        self.menu.pack()

        # self.gobutton = Button(self.title_page, text = 'Go!', command = self.startSearch, bg = 'white').pack()

        self.content_page = ttk.Frame(master)

        sportsData = msf('2018-2019-regular','full_game_schedule', 'KansasCity-Chiefs')
        self.currentWeek = sportsData['fullgameschedule']['gameentry'][12]

        self.title = ttk.Label(self.content_page, text = 'title', style = 'Header2.TLabel')
        self.title.grid(row = 0, column = 0, columnspan = 2)
        self.stats = ttk.Label(self.content_page, text = 'stats')
        self.stats.grid(row = 1, column = 0, sticky = 'w', padx = 5)
        self.weather = ttk.Label(self.content_page, text = 'weather')
        self.weather.grid(row = 1, column = 1, sticky = 'w', padx = 5)


        self.arrowheadTemp = Image.open('E:/school/2018-19/caps/A Foot in the Door/images/Arrowhead-Stadium_1490600234_96032.gif')
        self.arrowheadTemp = self.arrowheadTemp.resize((200,150), Image.ANTIALIAS)
        self.arrowheadTemp.save('E:/school/2018-19/caps/A Foot in the Door/images/Arrowhead-Stadium_1490600234_96032.gif', 'gif')
        self.arrowheadPic = PhotoImage(file = 'E:/school/2018-19/caps/A Foot in the Door/images/Arrowhead-Stadium_1490600234_96032.gif')

        self.metlifeTemp = Image.open('E:/school/2018-19/caps/A Foot in the Door/images/ezgif-2-9f29ee9de617.gif')
        self.metlifeTemp = self.metlifeTemp.resize((200,150), Image.ANTIALIAS)
        self.metlifeTemp.save('E:/school/2018-19/caps/A Foot in the Door/images/ezgif-2-9f29ee9de617.gif', 'gif')
        self.metlifePic = PhotoImage(file = 'E:/school/2018-19/caps/A Foot in the Door/images/ezgif-2-9f29ee9de617.gif')

        self.benzTemp = Image.open('E:/school/2018-19/caps/A Foot in the Door/images/ezgif-2-744eff298d4e.gif')
        self.benzTemp = self.benzTemp.resize((250,150), Image.ANTIALIAS)
        self.benzTemp.save('E:/school/2018-19/caps/A Foot in the Door/images/ezgif-2-744eff298d4e.gif', 'gif')
        self.benzPic = PhotoImage(file = 'E:/school/2018-19/caps/A Foot in the Door/images/ezgif-2-744eff298d4e.gif')


        self.arrowhead = ttk.Label(self.content_page, image = self.arrowheadPic)
        # self.arrowhead.grid(row = 2, column = 0, columnspan = 2)
        self.metlife = ttk.Label(self.content_page, image = self.metlifePic)
        # self.metlife.grid(row = 2, column = 0, columnspan = 2)
        self.benz = ttk.Label(self.content_page, image = self.benzPic)
        # self.benz.grid(row = 2, column = 0, columnspan = 2)

        self.backbutton = Button(self.content_page, text = 'Go Back', command = self.goBack)
        self.backbutton.grid(row = 3, column = 0, columnspan = 2)

    def startSearch(self, team):
        self.checkTeam = makeCompatable(team)
        sportsData = msf('2018-2019-regular','full_game_schedule', self.checkTeam)
        info = teamCity(team)
        IStadium = indoor()
        isindoor = FALSE
        self.currentWeek = sportsData['fullgameschedule']['gameentry'][13]

        # info = teamCity((self.currentWeek['homeTeam']['City'] + ' ' + self.currentWeek['homeTeam']['Name']))
        # self.weatherData = weather(info[0], info[1])

        if (self.currentWeek['awayTeam']['City'] + ' ' + self.currentWeek['awayTeam']['Name'] == team):
            self.title.config(text = team)
            self.stats.config(text = (str(self.currentWeek['date'])[5:7] + '/' + str(self.currentWeek['date'])[8:] +
                                        '\nAway Game\n'+ 'at ' + self.currentWeek['homeTeam']['City'] + ' ' + self.currentWeek['homeTeam']['Name']))
            
            if ((self.currentWeek['homeTeam']['City'] + ' ' + self.currentWeek['homeTeam']['Name']) in IStadium):
                isindoor = TRUE
            else:
                info = teamCity((self.currentWeek['homeTeam']['City'] + ' ' + self.currentWeek['homeTeam']['Name']))
                self.weatherData = weather(info[0], info[1])

        else:
            self.title.config(text = team)
            self.stats.config(text = (str(self.currentWeek['date'])[5:7] + '/' + str(self.currentWeek['date'])[8:] +
                                        '\nHome Game\n'+ 'vs ' + self.currentWeek['awayTeam']['City'] + ' ' + self.currentWeek['awayTeam']['Name']))
            if (team in IStadium):
                isindoor = TRUE
            else:
                info = teamCity(team)
                self.weatherData = weather(info[0], info[1])

        # print(self.weatherData)
        # print(self.currentWeek['homeTeam']['Name'] + self.currentWeek['awayTeam']['City'])

        self.month = str(self.currentWeek['date'])[5:7]
        self.day = str(self.currentWeek['date'])[8:]
        # self.weather.config(text = self.month)

        if (isindoor):
            self.weather.config(text = 'Indoor Stadium!')
        else:
            for i in self.weatherData['forecast']['simpleforecast']['forecastday']:
                if ((str(i['date']['day']) == self.day) and (str(i['date']['month']) == self.month)):
                    self.weather.config(text = ('High: ' + str(i['high']['fahrenheit']) + '°\n' + 'Low: ' + str(i['low']['fahrenheit']) + '°\n'
                                                    'Percipitation: ' + str(i['qpf_day']['in']) + ' in\n' + 'Snow: ' + str(i['snow_day']['in']) + ' in'))
                    # str(i['date']['pretty']) + 

        

        if ((team == 'Kansas City Chiefs') or (team == 'Los Angeles Chargers')):
            self.metlife.grid_forget()
            self.benz.grid_forget()
            self.arrowhead.grid(row = 2, column = 0, columnspan = 2)
        elif ((team == 'New York Giants') or (team == 'Tennessee Titans')):
            self.arrowhead.grid_forget()
            self.benz.grid_forget()
            self.metlife.grid(row = 2, column = 0, columnspan = 2)
        elif ((team == 'Atlanta Falcons') or (team == 'Arizona Cardinals')):
            self.arrowhead.grid_forget()
            self.metlife.grid_forget()
            self.benz.grid(row = 2, column = 0, columnspan = 2)
        else:
            self.arrowhead.grid_forget()
            self.metlife.grid_forget()
            self.benz.grid_forget()

        self.title_page.pack_forget()
        self.content_page.pack()

    def goBack(self):
        self.title_page.pack()
        self.content_page.pack_forget()

def main():            
    
    master = Tk()
    feedback = Feedback(master)
    master.mainloop()
    
if __name__ == '__main__': main()
