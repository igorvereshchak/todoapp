from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivymd.theming import ThemeManager
from kivymd.label import MDLabel

class ItemLabel(MDLabel):
    pass
        
    

class Container(BoxLayout):
    def addtodoClick(self, text):
        lab = ItemLabel(text="[ref=l]{}[/ref]".format(text))
        lab.font_size = '40sp'
        
        lab.bind(on_ref_press=self.LabelClickHandler)
        self.ids['todolist'].add_widget(lab)
        #print(self.ids['todolist'].children)
    
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
        lab.update()
        print("{} {}".format(lab.text_size, lab.texture_size))
        
             
    
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
    title = 'ToDo Application'

    
    
    
       
        

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        #self.theme_cls.primary_palette= 'Purple'
        c = Container()
        # for i in range(1, 6):
        #     lab = ItemLabel(text="[ref=l]Label{}[/ref]".format(i))
        #     lab.bind(on_ref_press=self.LabelClickHandler)
        #     c.ids['todolist'].add_widget(lab)
        return c    

if __name__ == "__main__":
    ToDoApp().run()        
#print("Hello, world")