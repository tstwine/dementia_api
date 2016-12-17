# #This is our decorator
# def simple_decorator(f):
#     # This is the new function we're going to return
#     # This function will be used in place of our original definition
#     def wrapper():
#         print "Entering Function"
#         f()
#         print "Exited Function"

#     return wrapper

# @simple_decorator 
# def hello():
#     print "Hello World"

# hello()


# def decorator_factory(enter_message, exit_message):
#     # We're going to return this decorator
#     def simple_decorator(f):
#         def wrapper():
#             print enter_message
#             f()
#             print exit_message

#         return wrapper

#     return simple_decorator

# @decorator_factory("Start", "End")
# def hello():
#     print "Hello World"

# hello()

# class NotFlask():
#     def __init__(self):
#         self.routes = {}

#     def route(self, route_str):
#         def decorator(f):
#             self.routes[route_str] = f
#             return f

#         return decorator

#     def serve(self, path):
#         view_function = self.routes.get(path)
#         if view_function:
#             return view_function()
#         else:
#             raise ValueError('Route "{}"" has not been registered'.format(path))


# app = NotFlask()

  


# # class TestNotFlask(unittest.TestCase):
# #     def setUp(self):
# #         self.app = NotFlask()

# #     def test_valid_route(self):
# #         @self.app.route('/')
# #         def index():
# #             return 'Hello World'

# #         self.assertEqual(self.app.serve('/'), 'Hello World')

# #     def test_invalid_route(self):
# #         with self.assertRaises(ValueError):
# #             self.app.serve('/invalid')

# # app = NotFlask()

# # app = Flask(__name__)

# @app.route("/hello/<username>")
# def hello_user(username):
#     return "Hello {} !".format(username)
    
