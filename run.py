import os
from app import db
from app.models import User
from utils.crud import query_all_users, query_all_questions, init_question_databse, init_user_databse, query_all_selected_questions, clear_all_selected_questions, clear_all_grades
from app import app as app_runner

# from utils.crud import clear_db
#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
	
    with app_runner.app_context():
        db.create_all()
        # new_user = User(id=1345, user='123456',password='1234646')
        # db.session.add(new_user)
        # db.session.commit()
        # clear_db(User)
        # query_all_users()
        # # insert_init_questions()
        # print(f"----------------------------------------------")
        # query_all_questions()
        init_user_databse()
        init_question_databse()

        clear_all_selected_questions()
        clear_all_grades()
        query_all_selected_questions()


    port = int(os.environ.get("PORT", 5000))
    app_runner.run(host='0.0.0.0', port=port)
