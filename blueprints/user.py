from flask import Blueprint
from flask import request
from mediators.userMediator import UserMediator

user = Blueprint('user', __name__)

@user.route('/user', methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        return UserMediator().hello()

