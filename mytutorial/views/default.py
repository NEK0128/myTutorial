from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import MyModel
import json


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(MyModel)
        one = query.filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'myTutorial'}

@view_config(route_name='foo', renderer='../templates/mytemplate.jinja2')
def foo_view(request):
    return Response("This is `foo` view", content_type='text/plain', status_int=200)

@view_config(route_name='bar' renderer='../templates/mytemplate.jinja2'))
def bar_view(request):
    return Response(json.dumps({"message":"This is `bar` message"}), content_type='application/json', status_int=200)


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_myTutorial_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
