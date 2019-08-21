from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window

from kivymd.theming import ThemeManager
from kivymd.label import MDLabel

import datetime
import locale

class ItemLabel(Label):
    pass
        
class ClickableImage(Image, ButtonBehavior):
    #def on_press(self):
    #    print(1)
    #def on_touch_down(self, touch): 
    pass
    
    

class Container(BoxLayout):
    
    stored_data = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(BoxLayout, self).__init__(*args, **kwargs)
        self.stored_data = JsonStore('data.json')
        for item_key in self.stored_data.keys():
            item = self.stored_data.get(item_key)
            self.addtodoClick(item['text'], item['done'])
        

    def addtodoClick(self, text, done=0):
        lab = ItemLabel(text="[ref=l]{}[/ref]".format(text))
        if done:
            lab.text = "[s]{}[/s]".format(lab.text)
            lab.color = (0.5, 0.5, 0.5, 1)
        lab.font_size = '40sp'
        
        lab.bind(on_ref_press=self.LabelClickHandler)
        lab.children[0].bind(on_touch_down=self.delClick)
        
        self.ids['todolist'].add_widget(lab)
        #self.ids['test_label'].text = lab.text
        #print("{}".format(lab.children[0].on_press()))
        #print(self.ids['todolist'].children)
    
    def delClick (self, image, touch):
        if image.collide_point(*touch.pos):
            #print(image.size)
            image.parent.parent.remove_widget(image.parent)
    

    def LabelClickHandler(self, *args):
        lab = args[0]
        text = lab.text
        if text.find('[s]')>=0:
            text = text.replace('[s]', '').replace('[/s]', '')
            lab.color = (1, 1, 1, 1)
        else:
            text = "[s]{}[/s]".format(text)
            lab.color = (0.5, 0.5, 0.5, 1)
        lab.text = text
        #locale.setlocale(locale.LC_TIME, 'ru')

        #print(time.strftime("%a %b %d %H:%M:%S %Y").encode('cp1251'))
        #lab.update()
        #print("{} {}".format(lab.text_size, lab.texture_size))
        
             
    
    def clearTodos(self):
        #print(self.ids['todolist'].children)
        gl = self.ids['todolist']
        #for lab in gl.children:
        while gl.children:
            lab = gl.children[0]
            #print(lab.text)
            gl.remove_widget(lab)
    

class ToDoApp(App):
    theme_cls = ThemeManager()
    locale.setlocale(locale.LC_TIME, 'ru')
    today = datetime.datetime.today().strftime("%A, %d.%m.%Y").encode('latin-1').decode('cp1251') # Finish
    title = 'Привет. Сегодня ' + today #time.strftime("%a %b %d %H:%M:%S %Y")
      
    def on_close(self, *args):
        key =  0
        self.root.stored_data.clear()
        for lab in self.root.ids['todolist'].children:
            self.root.stored_data.put(key, done=1 if "[s]" in lab.text else 0, \
                text=lab.text.replace("[s]", "").replace("[/s]", "").replace("[ref=l]", "").replace("[/ref]", ""))    
            key += 1

        return True   

    def build(self):
        Window.bind(on_close=self.on_close)
        self.theme_cls.theme_style = 'Dark'
        c = Container()
        return c    
    


if __name__ == "__main__":
    ToDoApp().run()        
#print("Hello, world")