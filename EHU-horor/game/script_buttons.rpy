define config.mouse = { }
# define config.mouse['default'] = [ ( "gui/cursor.png", 0, 0) ]
define config.mouse['loupe'] = [ ( "gui/loupe.png" , 16, 16) ]


screen info_panel_42:
  modal True
  frame:
    padding (10,10)
    xalign 0.95
    yalign 0.95
    xsize  250

    vbox:
      xsize 230
      text _("{size=24}{color=#555555}blabl{/color}{/size}") xalign 0.5
      null height 25
      textbutton _("Close") action Hide("info_panel_42") xalign 0.5

screen info_panel_51:
  modal True
  frame:
    padding (10,10)
    xpos 1323
    ypos 362
    xsize  250

    vbox:
      xsize 230
      text _("{size=24}{color=#555555}Войти{/color}{/size}") xalign 0.5
      null height 25
      textbutton _("Close") action Hide("info_panel_42") xalign 0.5


screen buttons_42:
  imagebutton:
    xpos 971
    ypos 255
    idle "/gui/button/42 button_hide.png"
    hover "/gui/button/42 button_show.png"
    action [ Show("info_panel_42")]
    hovered SetVariable("default_mouse", 'loupe')
    unhovered SetVariable("default_mouse", 'default')


screen buttons_51:
  imagebutton:
    xpos 1313
    ypos 322
    idle "/gui/button/51 location hallway button hide 1323x362 v2.png"
    hover "/gui/button/51 location hallway button show 1323x362 v2.png"
    action [ Show("info_panel_42")]
    hovered SetVariable("default_mouse", 'loupe')
    unhovered SetVariable("default_mouse", 'default')

screen buttons_11:
  imagebutton:
    xpos 272
    ypos 301
    idle "/gui/button/11 location room morning button hidden 301x272.png"
    hover "/gui/button/11 location room morning button show 301x272.png"
    action [ Show("info_panel_42")]
    hovered SetVariable("default_mouse", 'loupe')
    unhovered SetVariable("default_mouse", 'default')

screen buttons_13:
  imagebutton:
    xpos 1421
    ypos 203
    idle "/gui/button/13 location room v2 button hidden 1421x233.png"
    hover "/gui/button/13 location room v2 button show 1421x233.png"
    action [ Show("info_panel_42")]
    hovered SetVariable("default_mouse", 'loupe')
    unhovered SetVariable("default_mouse", 'default')