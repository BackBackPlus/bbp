from . import main
from .. import db
from ..models import User, Plan
from ..json_func import JsonFunc


@main.route('/<int:id>', methods=['POST'])
def home(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return JsonFunc.not_found()
    plan = Plan.query.filter_by(user_name=user.username)
    curr_plan = plan.query.order_by(plan.last_time.desc())
    return JsonFunc(name=user.username).return_json()

