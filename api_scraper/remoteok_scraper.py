import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate  # type: ignore

BASE_URL = "https://remoteok.com/api"
USER_AGERNT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
REQUEST_HEADER = {'User-Agent': USER_AGERNT,
                  'Accept-language': 'en-US,en;q=0.5'}


def get_job_postings():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER)
    return res.json()


if __name__ == "__main__":
    json = get_job_postings()[1]
    # print(get_job_postings())
    print(json)
