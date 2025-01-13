from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
helper=("""
ScreenManager:
    MenuScreen:
    CalciumScreen:
<MenuScreen>:
    name: 'main'
    MDScreen:
        rgba: app.theme_cls.surfaceColor

        MDBoxLayout:
            pos_hint: {"center_x": .5, "center_y": .7}
            size_hint: .8, .5

            FitImage:
                source: "logo.png"
                size_hint: .8, .4
                fit_mode: "fill"
            
        MDButton:
            style: "elevated"
            pos_hint: {"center_x": .5, "center_y": .3}
            on_press: root.manager.current = 'calcium'
            theme_width: "Custom"
            height: "40dp"
            size_hint_x: .6
           

            MDButtonText:
                text: "Star"
                pos_hint:{"center_x": .5 , "center_y": .5}

        MDLabel:
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .05}
            text: "powered By Ibn_Rushed co. all rights reserved © 2025"
            font_style: "Label"
            role: "small"
            
        

<CalciumScreen>:
    name :'calcium'
    MDScreen:
        md_bg_color: app.theme_cls.surfaceColor
       
        MDTopAppBar:
            type: "small"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .9}

            MDTopAppBarLeadingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "arrow-left"
                    on_press: root.manager.current = 'main'
                    on_press: root.clear()
            MDTopAppBarTitle:
                text: "Calcium Ionize"
                pos_hint: {"center_x": .5}

            

        
      
        MDBoxLayout:
            orientation: "vertical"
            spacing: "20dp"
            adaptive_height: True
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .65}

    
            MDTextField:
                id: cal
                
                
                MDTextFieldHintText:
                    text: "Calcium Total"

                MDTextFieldHelperText:
                    text: "Cacium total value im mg/dl"
                    mode: "on_error"

            MDTextField:
                id: alb
                
                MDTextFieldHintText:
                    text: "Albumin"

                MDTextFieldHelperText:
                    text: "Albumin value im mg/dl"
                    mode: "on_error"

        MDBoxLayout:
            orientation: "horizontal"
            spacing: "20dp"
            adaptive_height: True
            size_hint_x: .5
            pos_hint: {"center_x": .5, "center_y": .4}    
            MDButton:
                style: "elevated"
                pos_hint: {"center_x": .2, "center_y": .4}
                on_press: root.calc_i()
                theme_width: "Custom"
                height: "40dp"
                size_hint_x: .4


                MDButtonText:
                    text: "calculate"
                    pos_hint: {"center_x": .5, "center_y": .5}
            
            MDButton:
                style: "elevated"
                pos_hint: {"center_x": .7, "center_y": .4}
                on_press: root.clear()
                theme_width: "Custom"
                height: "40dp"
                size_hint_x: .4


                MDButtonText:
                    text: "Clear"
                    pos_hint: {"center_x": .5, "center_y": .5}
        MDLabel:
            id: result1
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .3}
            padding: "4dp", "4dp"

        MDLabel:
            id: result
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .2}
            allow_selection: True
            font_style: "Display"
            role: "small"
""")




# Declare both screens
class MenuScreen(Screen):
    pass

class CalciumScreen(Screen):
    def calc_i (self):
        try:
            calt = float(self.ids.cal.text)
            alb = float(self.ids.alb.text)
        
            
            
            if alb >= 3.5 :
                self.clc(calt,alb)
            else:
                self.calc(calt,alb)
        except ValueError:
            self.ids.result.text= ("Insert valid value" )
    def clc (self,cal,alb):
        cali = 0.25 * (0.9+(0.55*cal)-(0.3*alb))
        self.ids.result.text= str( cali)
        self.ids.result1.text= ("Calcium ionize is :" )
    def calc (self,cal,alb):
        cali = cal + (0.8 * (4 - alb))
        self.ids.result.text= str( cali)
        self.ids.result1.text= ("Calcium ionize is :" )

    def clear (self):
        self.ids.cal.text=""
        self.ids.alb.text=""
        self.ids.result.text=""
        self.ids.result1.text=""

     
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen())
sm.add_widget(CalciumScreen())


class TestApp(MDApp):

    def build(self):
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Darkblue"
        screen = Builder.load_string(helper)

        return screen

if __name__ == '__main__':
    TestApp().run()