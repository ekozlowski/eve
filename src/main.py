from eve import Eve

SETTINGS = {
    'DEBUG': True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite://',
    'DOMAIN': {
        'people': {},
        },
}

app = Eve(settings=SETTINGS)
app.run(host='0.0.0.0')