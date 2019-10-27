import requests
strs = "chalakkudi"
def api(river,place):
    url= "https://openhack-fac81.firebaseio.com/" + str(river)+"/"+str(place)+".json?orderBy=%22$key%22&limitToLast=1"
    response = requests.get(url)

    print(response.json())
    # print(url)


if __name__ == "__main__":
    pass
    api("chalakudi","meloor")



