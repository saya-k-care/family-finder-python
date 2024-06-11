import pymysql as MySQLdb;
import requests
# importing the requests library

class FamilyFinderRest:
    @staticmethod
    def get_address(lat, long):
        # api-endpoint
        URL = "https://nominatim.openstreetmap.org/reverse?email=pcyuen98@gmail.com&format=json&lat=" + lat + "&lon=" + long +"&addressdetails=1"
 
        # location given here
        location = "openstreetmap"
        
 
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'address':location}
 
        # sending get request and saving the response as response object
        r = requests.get(url = URL, params = PARAMS)
 
        # extracting data in json format
        data = r.json()
        print("---data=" , data);
 
# extracting latitude, longitude and formatted address
# of the first matching location
        display_name = data['display_name'];
 
        # printing the output
        print("display_name-->" + display_name)
        return display_name;
    