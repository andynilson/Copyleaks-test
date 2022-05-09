import base64
import random
from copyleaks.copyleaks import Copyleaks, Products
from copyleaks.exceptions.command_error import CommandError
from copyleaks.models.submit.document import FileDocument
from copyleaks.models.submit.properties.scan_properties import ScanProperties


# email address and api key
EMAIL_ADDRESS = 'andy.n@turing.com'
KEY = '767e3ba8-5f2f-4e59-830f-dfe826c50978'
PRODUCT = Products.BUSINESSES

try:
    auth_token = Copyleaks.login(EMAIL_ADDRESS, KEY)
except CommandError as ce:
    response = ce.get_response()
    print(f"An error occurred (HTTP status code {response.status_code}):")
    print(response.content)
    exit(1)

print("Logged successfully!\nToken:")
print(auth_token)


# This example is going to scan a file for plagiarism.
print("Submitting a new file...")
file_text = open('solutions/baseWhileLoopSolution.py', 'rb')
file_read = file_text.read()
BASE64_FILE_CONTENT = result = base64.b64encode(file_read).decode('ascii') # convert the file to base 64 format
FILENAME = "solutions/baseWhileLoopSolution.py"
scan_id = random.randint(100, 100000)  # generate a random scan id
file_submission = FileDocument(BASE64_FILE_CONTENT, FILENAME)

# send results of test to pipedream webhook
scan_properties = ScanProperties('https://eojs8lo649wa4pk.m.pipedream.net')
file_submission.set_properties(scan_properties)
Copyleaks.submit_file(PRODUCT, auth_token, scan_id, file_submission)  # sending the submission to scanning
print("Send to scanning")
print("You will be notified, using your webhook, once the scan was completed.")