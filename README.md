pip3 install --editable .

FLASK_APP=ahoy FLASK_DEBUG=true flask initdb

FLASK_APP=ahoy FLASK_DEBUG=true flask run
