#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from jsonLoader import msf, weather

class Feedback:

    def __init__(self, master):
        weatherData = weather('KS', 'Overland_Park')
        sportsData = msf('2018-2019-regular','full_game_schedule', 'losangeles-rams')

        master.title('Model')
        master.resizable(False, False)
        master.configure(background = '#ffffff')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#ffffff')
        self.style.configure('TButton', background = '#ffffff')
        self.style.configure('TLabel', background = '#ffffff', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 16, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        day = weatherData['forecast']['simpleforecast']['forecastday']
        header = ttk.Label(self.frame_header, text = (str(day[0]['date']['month']) + '/' + str(day[0]['date']['day']) + ' Conditions'),
                            style = 'Header.TLabel').pack()
        ttk.Label(self.frame_header, text = ('Temperature - High: ' + str(day[0]['high']['fahrenheit']) + '°, ' + 'Low: ' + str(day[0]['low']['fahrenheit']) + '°' +
                                            '\nPrecipitation - ' + str(day[0]['qpf_allday']['in']) + '"\n')).pack()


        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = ('Los Angeles Rams Schedule'),
                    style = 'Header.TLabel').pack()
        #content = ttk.Label(self.frame_content)
        #text = 'nothin'
        for i in sportsData['fullgameschedule']['gameentry']:
            if int(i['week']) < 10:
                if int(i['homeTeam']['ID']) == 77:
                    text = (content.cget('text') + 'Week ' + i['week'] + ': ' + '  vs ' + i['awayTeam']['City'] + ' ' + i['awayTeam']['Name'] + '\n')
                else:
                    text = (content.cget('text') + 'Week ' + i['week'] + ': ' + '  at ' + i['homeTeam']['City'] + ' ' + i['homeTeam']['Name'] + '\n')
                content.config(text = text)
            else:
                if i['homeTeam']['ID'] == '77':
                    text = (content.cget('text') + 'Week ' + i['week'] + ': ' + 'vs ' + i['awayTeam']['City'] + ' ' + i['awayTeam']['Name'] + '\n')
                else:
                    text = (content.cget('text') + 'Week ' + i['week'] + ': ' + 'at ' + i['homeTeam']['City'] + ' ' + i['homeTeam']['Name'] + '\n')
                content.config(text = text)
        content.pack(side = LEFT)



# https://stackoverflow.com/questions/19828054/python-pyinstaller-ioerror-errno-13-permission-denied
# Ask for admin password to run cmd in admin mode



def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == '__main__': main()
