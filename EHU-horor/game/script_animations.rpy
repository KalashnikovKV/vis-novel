
# image model_bus =  SnowBlossom('33_location_busstop_model_bus', count=1, xspeed=(-200), yspeed=(0), horizontal=True)


# Анимация
image menu_slideshow:
    "basement_dark_lights_on_off" 
    pause 2.5
    "basement_dark_lights_on_off" 
    pause 2.5
    # "images/1_act/fon/locations/02 cover basement dark lights off 1f.jpg" 
    # pause 1.0
    # "images/1_act/fon/locations/02 cover basement dark 00.jpg" 
    # pause 2.0
    # "images/1_act/fon/locations/02 cover basement dark lights off 1.jpg" 
    # pause 2.0
    "images/1_act/fon/locations/02 cover basement dark lights on 1.jpg"
    pause 2.5
    # "images/1_act/fon/locations/02 cover basement dark lights off 1s.jpg" 
    # pause 1.0
    "basement_dark_lights_on_off" 
    pause 2.5
    repeat


image basement_silhouettes:
    pause 1.0
    "/images/1_act/fon/silhouettes/02 сover basement silhouettes 1.png" 
    pause 1.0
    "/images/1_act/fon/silhouettes/02 сover basement silhouettes 2.png" 
    repeat


image basement_dark_lights_on_off:
    "images/1_act/fon/locations/02 cover basement dark lights on 1.jpg" 
    choice:
        pause 0.5
    choice:
        pause 1.0
    choice:
        pause 1.5
    "images/1_act/fon/locations/02 cover basement dark lights off 1.jpg" 
    pause 1.0

# image 33_location_busstop_model_bus:
#     "/images/1_act/fon/silhouettes/33 location busstop model bus.png" 
#     pause 3.0