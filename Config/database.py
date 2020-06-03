import mongoengine


def global_init():
    mongoengine.register_connection(alias='core', name='todo_list')
    # mongoengine.connect('todo_list', alias='core')

