import pyweber as pw
from componentes.components import Main

app = pw.Pyweber()

class Todo(pw.Template):
    def __init__(self):
        super().__init__(template='', title='Todo App')
        self.head.add_child(pw.Style(href='../app/src/style.css'))
        self.body.add_child(Main())

@app.route('/')
def home():
    return Todo()

if __name__ == '__main__':
    pw.run()