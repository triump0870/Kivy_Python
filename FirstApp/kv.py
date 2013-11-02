from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
FloatLayout:
	canvas.before:
		Color:
			rgba: 0 ,1, 0, 1
		Rectangle:
			# Self here refers to the widget i.e FloatLayout
			pos: self.pos
			size: self.size
	Button:
		text: 'Hello World!!'
		size_hint: .5,.5
		pos_hint: { 'center_x':.5 ,'center_y': .5}
''')

class MainApp(App):
	def build(self):
		return root

if __name__ == '__main__':
	MainApp().run()
