import pyweber as pw
import asyncio

class Title(pw.Element):
    def __init__(self, content: str):
        super().__init__(tag='h2', content=content, classes=['title'])

class InputText(pw.Element):
    def __init__(self, placeholder: str):
        super().__init__(
            tag='input',
            id='new-task',
            attrs={
                'placeholder': placeholder,
                'type': 'text',
                'name': 'new-task'
            }
        )

class InputButton(pw.Element):
    def __init__(self, value: str):
        super().__init__(
            tag='input',
            classes=['btn', 'btn-submit'],
            value=value,
            attrs={'type': 'submit', 'name': 'submit'}
        )
        self.events.onclick = self.create_task
    
    async def create_task(self, e: pw.EventHandler):

        if e.element.parent.childs[0].value.strip():
            e.template.querySelector('.tasks').add_child(
                Task(task='Processing...')
            )

            e.update()

            e.template.querySelectorAll(
                '.task-text'
            )[-1].content = e.element.parent.childs[0].value
        
        e.element.parent.childs[0].value = ''

        e.update()

class InputGroup(pw.Element):
    def __init__(self):
        super().__init__(tag='div', classes=['input-group'])
        self.childs = [
            InputText(placeholder='write your task here...'),
            InputButton(value='Create')
        ]

class TaskActions(pw.Element):
    def __init__(self):
        super().__init__(tag='div', classes=['task-actions'])
        self.childs = [
            pw.Element(
                tag='button',
                content='Edit',
                classes=['btn', 'btn-edit'],
                events=pw.TemplateEvents(onclick=self.edit)
            ),
            pw.Element(
                tag='button',
                content='Delete',
                classes=['btn', 'btn-delete'],
                events=pw.TemplateEvents(onclick=self.delete)
            )
        ]
    
    def get_clicked_element(self, e: pw.EventHandler):
        return e.element.parent.parent
    
    def edit(self, e: pw.EventHandler):
        task = self.get_clicked_element(e)
        input_text = e.template.querySelector('#new-task')
        input_text.value = task.childs[0].content

        task.parent.childs.remove(task)
        e.update()

    def delete(self, e: pw.EventHandler):
        task = self.get_clicked_element(e)
        task.parent.remove_child(task)
        e.update()

class Task(pw.Element):
    def __init__(self, task: str):
        super().__init__(tag='div', classes=['task'])
        self.childs = [
            pw.Element(tag='p', content=task, classes=['task-text']),
            TaskActions()
        ]

class Tasks(pw.Element):
    def __init__(self):
        super().__init__(tag='div', classes=['tasks'])

class Main(pw.Element):
    def __init__(self):
        super().__init__(tag='main')
        self.childs = [
            Title(content='Todo App'),
            InputGroup(),
            Tasks()
        ]