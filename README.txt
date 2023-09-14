Test the Email Parser service.

To visually test Email Parser open the web page 
http://3.227.179.42/

You can pick 'test subject.eml' file from the current folder or load other .eml file (you can load any email file on your PC, for example from gmail. Check 'download_email_file.jpg').

To test the API function in python script open current folder in the console and enter the following

pip install -r requirements.txt
python test_email_parser.py

parsing result should be in the result.json file.

You can change variable 'path_to_email' in test_email_parser.py file to check parsing of other email file.
