# @app.route('/', methods=['POST', 'GET'])
# def home():
#     search = Search.query.all()
#     form = AddressForm(request.form)

#     if request.method == 'POST' and form.validate():
#         newSearch = Search(city=form.city.data, state=form.city.data, zip=form.city.data)    

#         return redirect(url_for('search'))

#     return render_template('home.html', search=search, form=form)    


# cur.execute""" % (city, state)

# SELECT id, name, city, state 
        # FROM memory_care_facilities 
        # WHERE city = %s AND state = %s;   
import psycopg2

city = 'Miami'
state = 'FL'

conn = psycopg2.connect(database="testdb", user="tinastith-twine", host="127.0.0.1", port="5432")
cur = conn.cursor()
#query= "city, state" 
name = []
cur.execute("SELECT * FROM memory_care_facilities WHERE city = '%s' AND state = '%s';" %(city, state)) 

data = cur.fetchall()
#rows_to_fetch = 3
#print cur.fetchmany(rows_to_fetch)
conn.close
#print cur.fetchall()
print data