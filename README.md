# elasticemail-django

Simple django backend to send email through [Elasticemail](https://elasticemail.com) as your EmailBackend.

1. Install the package via pip `pip install -e git+https://github.com/muepsilon/elasticemail-django#egg=elasticemail-django`

2. Add `elasticemailbackend` to `INSTALLED_APPS`

3. In `settings.py` add: 
    `ELASTICEMAIL_API_KEY = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"`
    `EMAIL_BACKEND = "elasticemailbackend.backend.ElasticEmailBackend"`
    `DEFAULT_FROM_EMAIL = "test@example.com"`

