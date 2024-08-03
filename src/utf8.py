import re


class GetAccessTest:
    @staticmethod
    def getUser(log_entry, access_set):
        # Split the log entry by spaces
        log_parts = log_entry.split()

        # Extract the last string (IP address)
        ip_address = log_parts[-1]

        # Extract the date and time using regular expression
        datetime_pattern = r'\[(.*?)\]'
        match = re.search(datetime_pattern, log_entry)
        
        if match:
            date_and_time = match.group(1)
            date_time_str = date_and_time[12:17]  # Extract characters between positions 12 and 17
            print(f'Extracted Date and Time: {date_time_str}')
        else:
            print('Date and Time not found in the log entry.')
            return

        start_index = log_entry.find("http")
        http_string = None

        # Find the position of the closing double quote after "http"
        if start_index != -1:
            end_index = log_entry.find('"', start_index)
            if end_index != -1:
                http_string = log_entry[start_index:end_index]
                if "undefined" in http_string or "news" in http_string or "gospel" in http_string:
                    print(f'String starting with "http": {http_string}')
                else:
                    http_string = None

        if http_string is not None:
            user = f"[TIME]={date_time_str} [URL]={http_string} [IP]={ip_address}"

            access_set.add(user)
            #print("User-->", user)
        return access_set

# Call the getUser method with the log entry
log_entry = '172.68.26.155 - - [02/Aug/2024:03:51:27 +0800] "GET /8805.878a297709031db8.js HTTP/1.1" 200 6415 "http://eyebot.name.my/map/undefined" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/126.0.6478.182 Safari/537.36" "66.249.65.198"'

access_set = set()
access_set = GetAccessTest.getUser(log_entry,access_set)
print(access_set)
print(f"Total Users={len(access_set)}")