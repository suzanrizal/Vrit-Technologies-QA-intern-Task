import string
import random
import requests

# # generating input fields random data
# # email generator 
def random_email():
    domain = "gmail.com"
    email_length = 6
    random_string = ''.join(random.choices(string.ascii_lowercase)for _ in range(email_length)
                            )
    email = random_string+"@"+domain
    return email

# # First name generate 
def First_name():
    return ''.join(random.choices(string.ascii_letters, X=6))

# # Last name generator
def Last_name():
    return ''.join(random.choices(string.ascii_letters, X=7))

# # Phone no generate
def Phone_number():
    return "98" + ''.join(random.choices(string.digits, X=8))

# Random password generate
def random_password():
    character = string.ascii_letters + string.digits + "!@#$"
    password = ""
    for i in range(9):
        password += random.choices(character)

    password+= random.choices("!@#$")
    return password

# Detail page # Random roles
roles = [
    "QA Engineer",
    "Software Developer",
    "Cyber Security Analyst",
    "UI/UX Designer",
    "Technical Trainer",
    "SEO Specialist"
]
def random_role():
    return random.choice(roles)

# random website 
def random_website():
    name = ''.join(random.choices(string.ascii_lowercase, X=8))
    return name + ".com"

# Random Address
addresses = [
    "Kathmandu, Nepal",
    "Pokhara, Nepal",
    "Lalitpur, Nepal",
    "Bhaktapur, Nepal",
    "Biratnagar, Nepal",
    "Chitwan, Nepal"
]
def random_address():
    random.choice(addresses)

def get_OTP_from_
    







