#web Api test for iss_now using requests
# we added the json module to use the json file as a dictionary file
# we add the turtle module to plot the location of the ISS.

import requests, json, turtle

iss=turtle.Turtle()

def setup(window):
    global iss
    window.setup(1000,500)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180,-90,180,90)
    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')
#to change the turtle shape from circle to iss photo, we need to register a new shape
#iss.color('red')
def move_iss(lat,long):
    global iss

    iss.hideturtle()
    
    iss.goto(long, lat)
    iss.pendown()
    iss.showturtle()

def track_iss():
    url='http://api.open-notify.org/iss-now.json'
    response=requests.get(url)
    if (response.status_code==200):
# print(response.text)
        response_dictionary = json.loads(response.text)
        position=response_dictionary['iss_position']
    #print('International Space Station is right now at '+position['latitude']+', '+position['longitude'])

        lat=float(position['latitude'])
        long=float(position['longitude'])
        move_iss(lat,long)
    else:
        print('Houston, we have a problem:',response.status_code)
    widget = turtle.getcanvas()
    widget.after(5000, track_iss)

def main():
    global iss
    screen=turtle.Screen()
    setup(screen)
    track_iss()

if __name__=='__main__':
    main()
    turtle.mainloop()
