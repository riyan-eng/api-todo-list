from app import app
from app.controllers import authentication, profile, token, task


app.route("/users/register", methods=["POST"])(authentication.register)
app.route("/users/login", methods=["POST"])(authentication.login)
app.route("/", methods=["GET"])(profile.Profile)
app.route("/refresh", methods=["POST"])(token.refresh)
# app.route("/logout", methods=["DELETE"])(token.logout)

app.route("/task/list", methods=["POST"])(task.list)
app.route("/task/create", methods=["POST"])(task.create)
app.route("/task/detail/<taskId>", methods=["GET"])(task.read)
app.route("/task/update/<taskId>", methods=["PUT"])(task.update)
app.route("/task/delete/<taskId>", methods=["DELETE"])(task.delete)