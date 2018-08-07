# nextbigsound-python-client
Next Big Sound Python client

## Requirements

1. Verify python 2.7 version `python --version`

2. Verify pip 9 version `pip2 --version`

3. Verify virtualenv 15 version `virtualenv --version`

Note: If one missed install it via `brew` or `easy_install` (install global packages like `virtualenv`) and `pip` (install python packages in a local environment)

## Virtual Environment

1. Create a virtual environment `mkvirtualenv nextbigsound-python-client`

2. `cd nextbigsound-python-client`

3. Activate the virtual environment `workon nextbigsound-python-client`

4. Install the dependencies `pip2 install -r requirements.txt`

5. Deactivate virtual environment once done `deactivate`

## Getting artists with NextBigSound API

1. Add the token in the env variables to be used in the python script `export NEXT_BIG_SOUND_TOKEN="YOUR_PRIVATE_TOKEN"`

2. Test `python test_client.py`, getting charts, releases, appearances and then artists.

3. Test `python test_client_2.py`, getting artists directly by genering the ids automatically.
