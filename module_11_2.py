import inspect

info_in_internet = ['introspection', 'classes', 'functions', 'multiprocessing']


class HomeWork:
    def __init__(self, task_number, task_topic, difficult):
        self.task_topic = task_topic
        self.task_number = task_number
        self.difficult = difficult

    def search_info(self):
        for topic in info_in_internet:
            if topic is self.task_topic:
                return True

        return False

    def solution(self):
        if self.search_info():
            print(f'По теме {self.task_topic} есть информация в интернете. Задачу можно решить')
        else:
            print(f'По теме {self.task_topic} нет информации в интернете. Попробуйте поискать в библиотеке ;)')


hw1 = HomeWork(1, 'introspection', False)


def introspection_info(object_):
    type_ = type(object_)
    list_args = [i for i in dir(object_) if not callable(getattr(object_, i))]
    list_methods = [i for i in dir(object_) if callable(getattr(object_, i))]
    module = inspect.getmodule(object_)
    id_ = id(object_)
    is_class = inspect.isclass(object_)
    is_module = inspect.ismodule(object_)
    is_builtin = inspect.isbuiltin(object_)
    return {'type': type_.__name__, 'attributes': list_args, 'methods': list_methods, 'module': module, 'id': id_,
            'is_class': is_class, 'is_module': is_module, 'is_builtin': is_builtin}


res = introspection_info(hw1)
print(res)

