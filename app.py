import streamlit as st

import os

st.title('배포 테스트')
st.write('배포 테스트용 앱')

st.write('추가 커밋')

api_key = os.environ.get('API_SECRET_KEY')

st.write(f'api key = {api_key}')

if not os.environ.get('DB_HOST'):
    st.write('DB 정보가 없음')
else:
    conn = pymysql.connect(host=os.environ.get('API_SECRET_KEY'))