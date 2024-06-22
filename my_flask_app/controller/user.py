from flask import Blueprint,render_template
user=Blueprint("user",__name__)

@user.route("/user/login")
def login():
    return "登入成功"

@user.route("/user/info")
def info():
    return render_template("user_info.html",
                           name="Scott",
                           sex="male",
                           age=26,
                           tel=["095456156","054841298"])