# Email Sender Script

## Description
This application sends HTML emails using a specified template. The script loads credentials from a `.env` file, reads an HTML template, and sends the email to the specified recipient.

## Requirements
- Python 3.6 or higher
- Libraries specified in `requirements.md`


## Installation
1. Clone the repository:
    ```sh
    git clone <REPOSITORY_URL>
    cd emails-html-python
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```


3. Install the dependencies:
    ```sh
    pip install -r requirements.md
    ```

4. Create a `.env` file in the root of the project with the following content:
    ```env
    EMAIL=your_email@gmail.com
    PASSWORD=your_password
    ```

## Usage
To send an email, run the [main.py](http://_vscodecontentref_/1) script with the required arguments:

```sh
python main.py -e recipient@example.com -s "Email Subject" -f "path/to/email.html"