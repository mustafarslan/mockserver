from controllers.userController import UserController


class UserMediator(object):
    def getUser(self):
        return UserController().getUser()


    def postUser(self):
        return UserController().postUser()