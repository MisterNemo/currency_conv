**run project:**

`docker-compose build`

`docker-compose up -d`

`docker-compose run app python manage.py makemigrations`

`docker-compose run app python manage.py migrate`

`docker-compose run app python manage.py manual_request`


**Test:**

`docker-compose run app pytest`

**Requests example:**

**Get currencies list:**

_GET: /api/v1/currencies/_

**Get rate example:**

_POST /api/v1/currencies/ HTTP/1.1
Host: localhost
Content-Type: application/json
{
	"from_curr": "EUR",
	"to_curr": "PLN",
	"from_amount": 112
}_