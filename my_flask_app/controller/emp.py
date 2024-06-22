from flask import Blueprint,render_template
import db.emp

emp=Blueprint("emp",__name__)

@emp.route("/emp/search-emp-list")
def search_emp_list():
    list=db.emp.get_user_details()
    return render_template("emp.html",list=list)