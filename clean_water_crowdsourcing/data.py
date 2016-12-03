from models import Account
from models import WaterPurityReport
from models import WaterSourceReport

Account.objects.create(first_name="A", last_name="User", email="user@gatech.edu", password="pass", username="user", phone="0000000000"
                       , address_street="123", address_city="Atlanta", address_state="GA", address_zip="30303", account_type="User")
Account.objects.create(first_name="A", email="worker@gatech.edu", last_name="Worker", password="pass", username="worker", phone="0000000000"
                       , address_street="123", address_city="Atlanta", address_state="GA", address_zip="30303", account_type="Worker")
Account.objects.create(first_name="A", email="manager@gatech.edu", last_name="Manager", password="pass", username="manager", phone="0000000000"
                       , address_street="123", address_city="Atlanta", address_state="GA", address_zip="30303", account_type="Manager")
Account.objects.create(first_name="An", email="admin@gatech.edu", last_name="Admin", password="pass", username="admin", phone="0000000000"
                       , address_street="123", address_city="Atlanta", address_state="GA", address_zip="30303", account_type="Administrator")
Account.objects.create(first_name="Sruti", email="sruti@gatech.edu", last_name="Guhathakurta", password="pass", username="SrutiG", phone="0000000000"
                       , address_street="351 Sinclair Ave NE", address_city="Atlanta", address_state="GA", address_zip="30307", account_type="Manager")
account = Account.objects.get(username="user")
WaterSourceReport.objects.create(reporter_name=account, water_type="Bottled", water_condition="Waste",
                                 water_location="351 Sinclair Ave NE, Atlanta, GA 30307")
WaterSourceReport.objects.create(reporter_name=account, water_type="Stream", water_condition="Potable",
                                 water_location="North Ave NW, Atlanta, GA 30332")