import requests
import json
import urllib.request

def printData(url, filePath):
    jsonData = json.loads(url)

    # print("________________\n10-Day Forecast\n________________\n")

    # for i in jsonData["forecast"]["simpleforecast"]["forecastday"]:
    #         print(i["date"]["weekday"], i["date"]["month"], "/", i["date"]["day"], "/", i["date"]["year"])
    #         print("High Temp: ", i["high"]["fahrenheit"], "°")
    #         print("Low Temp: ", i["low"]["fahrenheit"], "°")
    #         print("Precipitation: ", i["qpf_allday"]["in"], "\"")
    #         print("________________")

    with open(filePath, "w+") as f:

        f.write("________________\n10-Day Forecast\n________________\n")

        for i in jsonData["forecast"]["simpleforecast"]["forecastday"]:
            if(i["period"] > 1): f.write("\n")
            f.write(str(i["date"]["weekday"]) + ": " + str(i["date"]["month"]) + "/" + str(i["date"]["day"]) + "/" + str(i["date"]["year"]) + "\n")
            f.write("High Temp: " + str(i["high"]["fahrenheit"]) + "°" + "\n")
            f.write("Low Temp: " + str(i["low"]["fahrenheit"]) + "°" + "\n")
            f.write("Precipitation: " + str(i["qpf_allday"]["in"]) + "\"" + "\n")
            f.write("________________")

def main():
    url = "http://api.wunderground.com/api/b965ca79c6a364e1/forecast10day/q/MO/Kansas_City.json"
    webUrl = urllib.request.urlopen(url)
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printData(data, "E:/school/2018-19/caps/A Foot in the Door/results/10day.txt")
    else:
        print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

if __name__ == "__main__":
    main()