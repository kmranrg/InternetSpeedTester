# Python program to test
# internet speed

import speedtest


st = speedtest.Speedtest()

option = int(input('''What speed do you want to test:

1) Download Speed

2) Upload Speed

3) Best Ideal Server

Your Choice: '''))


if option == 1:

    download_speed = st.download()/1024/1024
    print(f"Download Speed: {download_speed: .3f} Mbps")

elif option == 2:

    upload_speed = st.upload()/1024/1024
    print(f"Upload Speed: {upload_speed: .3f} Mbps")

elif option == 3:

    ideal_server = st.get_best_server()
    print("Best Ideal Server:")
    print("\tCity:",ideal_server["name"])
    print("\tCountry:",ideal_server["country"])
    
    '''
    NOTE: get_best_server() returns a dictionary

    1) lat: for getting the latitude
    2) lon: for getting the longitude
    3) name: for getting the city name
    4) country: for getting the country name
    5) cc: for getting the country code
    '''

else:

	print("Please enter the correct choice !")
