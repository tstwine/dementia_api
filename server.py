
from imports import *
from forms import AddressForm
import lob
lob.api_key = 'test_769532f5a1902f3bbffbf3235236c58268d'                                                                                                                                                                                                                
app = Flask(__name__, static_folder='static')
app.config.from_pyfile("settings/config.py")

auth = HTTPBasicAuth()




@auth.get_password
def get_password(username):
    if username == 'tina':
        return 'dementia'
    return None 

# memory route
@app.route('/dementia_types/<int:dementia_type_id>')
def get_dementia_type(dementia_type_id):

    conn = psycopg2.connect(database="testdb", user="tinastith-twine", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute('SELECT * FROM memory WHERE id=%s;' %dementia_type_id)
    data = cur.fetchall()
    conn.close
    #print data
    return render_template("information.html", data=data[0])



# comment route query
@app.route('/')
def home():
    #from models import db, Comment
    conn = psycopg2.connect(database="testdb", user="tinastith-twine", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM memory;')
    data = cur.fetchall()
    conn.close
    #print data
    #comments = Comment.query.all() # this code is used for SQLAlchemy only.
    
    return render_template('home.html', dementia_types=data)

# memory_care_facilities query
@app.route('/search/', methods=['GET','POST'])
def search():
    new_data = []
    error = None
    if request.method == 'POST': # if someone submits a POST on this page. 
        address = request.form['addressLine1']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipCode']

        try:
            
            verify_address = lob.Verification.create(
                address_line1=address,
                address_city=city,
                address_state=state,
                address_zip=zipcode,
            )

            #print verify_address

            city = verify_address['address']['address_city'].title()
            state = verify_address['address']['address_state']

            conn = psycopg2.connect(database="testdb", user="tinastith-twine", host="127.0.0.1", port="5432")
            cur = conn.cursor() 
            cur.execute("SELECT * FROM memory_care_facilities WHERE city = '%s' AND state = '%s';" %(city, state)) 
            data = cur.fetchall()
            conn.close

            #print data

            for memory_care_facility in data:
                new_row = []
                for item in memory_care_facility:
                    new_item = str(item).strip().replace("\xe2\x80\x99", "'")
                    new_row.append(new_item)
                new_data.append(new_row)

            #print new_data
        except Exception as error:
            pass

    return render_template('search.html', data=new_data, error=error)

# senior_day_center query
@app.route('/senior/', methods=['GET', 'POST'])
def senior():

    senior_data = []
    error = None

    if request.method == 'POST':
        address = request.form['addressLine1']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipCode']

        try:

            verify_address = lob.Verification.create(
                address_line1=address,
                address_city=city,
                address_state=state,
                address_zip=zipcode
            )

            #print verify_address

            city = verify_address['address']['address_city'].title()
            state = verify_address['address']['address_state']

            conn = psycopg2.connect(database="testdb", user="tinastith-twine", host="127.0.0.1", port="5432")
            cur = conn.cursor() 
            cur.execute("SELECT * FROM senior_day_centers WHERE city = '%s' AND state = '%s';" %(city, state)) 
            data = cur.fetchall()
            conn.close

            #print data

            for senior_day_center in data:
                new_row = []
                for item in senior_day_center:
                    new_item = str(item).strip().replace("\xe2\x80\x99", "'")
                    new_row.append(new_item)
                senior_data.append(new_row)

            #print senior_data

        except Exception as error:
            pass

    return render_template('senior.html', data=senior_data, error=error)

# # login route
# @app.route('/comment', methods=['GET', 'POST'])
# def createComment():

#     name = request.form.get("name")
#     text = request.form.get("text")

#     from models import db, Comment 

#     comment = Comment(name, text)
#     db.session.add(comment)
#     db.session.commit()

#     return render_template('comment.html', comment=comment)

# @app.route('/post', methods=["GET", "POST"])
# def createPost():
#     title = request.form.get("title")
#     author = request.form.get("author")
#     text = request.form.get("text")

#     from models import db, post

#     post = Post(title, author, text)
#     db.session.add(post)
#     db.session.commit()

#     comments = Comment.query.all()
#     return render_template('blog.html', post=post)




# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/blog', methods=['GET', 'POST'])
def blog():

    from models import db, Post, Comment    

    if request.method == 'POST':
        
        #print request.form

        

        title = request.form.get('title')
        text = request.form.get('text')
        author = request.form.get('author')
        post = Post(title,text,author)
        db.session.add(post)
        db.session.commit()

        #print post

    posts = Post.query.all()

    return render_template('blog.html', posts=posts)  




@app.route('/brain_tour')
def brain_tour():
    brain = "alzheimers"
    return render_template('brain.html', brain=brain)

@app.route('/ebook')
def ebook():
    ebook = "caring for alzheimers"
    return render_template('ebook.html', ebook=ebook)


    

if __name__ == '__main__':
    app.run(debug=False)  



    