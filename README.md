# FLASKAPI_SMP
 Python Flask along with SQL Alchemy and Marshmallow to create a RESTful API for products.
 
 
# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py
```

## Endpoints

* GET     /product
* GET     /product/:id
* POST    /product
* PUT     /product/:id
* DELETE  /product/:id
