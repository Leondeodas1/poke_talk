from flask_app import app 
from flask_app.controllers import login_reg_controller
from flask_app.controllers import user_controller
from flask_app.controllers import profile
from flask_app.controllers import create_a_post
from flask_app.controllers import messages_controller


if __name__ == "__main__":
    app.run(debug=True)