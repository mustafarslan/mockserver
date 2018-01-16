from controllers.userController import TEST


class UserMediator(object):
    def hello(self):
        str = TEST().test()
        return str + " Mediator"