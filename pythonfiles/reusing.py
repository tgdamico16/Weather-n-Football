from weatherTesting import printData
import urllib.request


def main():
    url = "http://api.wunderground.com/api/b965ca79c6a364e1/forecast10day/q/MO/Kansas_City.json"
    webUrl = urllib.request.urlopen(url)
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printData(data, "E:/school/2018-19/caps/A Foot in the Door/results/10dayy.txt")
    else:
        print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

if __name__ == "__main__":
    main()