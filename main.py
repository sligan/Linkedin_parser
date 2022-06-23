import requests
from bs4 import BeautifulSoup

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
ASPIRING_DATA_SCIENTIEST = 'https://www.linkedin.com/in/alexandr-sligan-a2637b1b4/'

# get url, soup object and csrf token value
html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "html.parser")

login_information = {
    'session_key': 'grand91@inbox.ru',
    'session_password': '16925410791'
}

try:
    client.post(LOGIN_URL, data=login_information)
    print("Login Successful")
except:
    print("Failed to Login")

headers = {
    'Host': 'www.linkedin.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': 'bcookie="v=2&38eac028-6004-493f-8256-f55ddf8032d5"; '
              'bscookie="v=1&202206231356469ba505a8-c09a-4840-8cfa-525e74407761AQG0Odec9o09YsVuRgSPOggpJw8CZ2Ej"; '
              'li_gc=MTsyMTsxNjU1OTkyNjExOzI7MDIxwxXeQc7y47XOTJynY9D/ncaPAq2gJWNu76416zvPByw=; '
              's_fid=23E56042A24B940A-2EFB5C6085D2AAAA; s_cc=true; at_check=true; li_alerts=e30=; '
              'AMCVS_14215E3D5995C57C0A495C55@AdobeOrg=1; G_ENABLED_IDPS=google; '
              'aam_uuid=40778524994626030360824645215467716114; '
              'li_at=AQEDATHjav4BlpQxAAABgZFRyQIAAAGBtV5NAk0ASi1u_hPKCMV7uDbiLnjzVcsFF56Vbcw9oYXjYxIqb22CvaDDoh_I2gZGalKFR53Za-3mBY-2_iIbCNP1RuJANmRtdmFXdFGQncVT2MHvJdipbSN3; liap=true; JSESSIONID="ajax:5664800587413324780"; lang=v=2&lang=ru-ru; timezone=Asia/Novosibirsk; li_theme=light; li_theme_set=app; AnalyticsSyncHistory=AQKMnhAJ4VuZTwAAAYGRUsS2tzStEKEs4Gm43W-ti25sma8_07medXAKLojvzEGFCtYFcpGnscNo8ijCzo6lDw; _guid=2a0606b8-1e83-49ba-a699-5d34f127c3fe; lms_ads=AQH8rPk9Fn6WCQAAAYGRUsYurhyrvAY59swZVsBVMzCQTy7kaBMWsl8I8KuTGJoQQSYL0Du7ouR1-v5zvov7xgNAMsmf_9Ch; lms_analytics=AQH8rPk9Fn6WCQAAAYGRUsYurhyrvAY59swZVsBVMzCQTy7kaBMWsl8I8KuTGJoQQSYL0Du7ouR1-v5zvov7xgNAMsmf_9Ch; AMCV_14215E3D5995C57C0A495C55@AdobeOrg=-637568504|MCIDTS|19167|MCMID|40600984291751165030846277920511970777|MCAAMLH-1656605330|6|MCAAMB-1656605330|6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y|MCOPTOUT-1656007730s|NONE|vVersion|5.1.1|MCCIDH|845969833; s_sq=[[B]]; gpv_pn=developer.linkedin.com/product-catalog; s_tp=5029; s_plt=0.32; s_pltp=developer.linkedin.com/product-catalog; s_ips=4816; s_ppv=developer.linkedin.com/product-catalog,96,96,4816,6,6; mbox=PC#5b72a339cdd045a0839d9a5f0c41f03d.37_0#1671553977|session#55183b801b1e490c860676e590fdbe23#1656003798; s_tslv=1656001978669; li_mc=MTsyMTsxNjU2MDA1MjUyOzI7MDIxDEbawwXSqfL654x3gomYX155waqjVU5FVpGtEngiW8o=; UserMatchHistory=AQKpshUJFxv2XgAAAYGRoanJfgf7NAFm0Bhf0m7czuoFe7zu_WhOF8h03lvvPKhPJvffF0FDlD1tGafl0r65p0_Y8TkhRH7mlmkf_qVOn3dtImBNNyggc63iOj2pjFSALPEGO_QLVon3yjsCq_CRV50kpGh8jf5YxBPfq1V8NWLubo40_8OGz9gsVtc1DIQGcaf-OuIioRUFfdMEa_DWNIM3i8pWJCXVrpsO3zfBqvAAnUfD440HEhEz5Esdvg4DjTnZZT7x6paVYVXe81o3GZ_PnXXMa7pBXZcNqR4; lidc="b=OB46:s=O:r=O:a=O:p=O:g=3069:u=84:x=1:i=1656005703:t=1656007059:v=2:sig=AQG1CN91Fqcx8QvVl6XW0FygEucK26El"',

    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'
}

r = requests.get(
    'https://www.linkedin.com/company/digitalpik/', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
users_count = soup.find_all('div', class_ = 'org-top-card-summary-info-list__info-item')
print(users_count)
