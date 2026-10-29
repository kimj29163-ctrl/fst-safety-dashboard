import requests

# 국가법령정보 공동 활용(Open API) 승인키 (OC)
API_KEY = "FST0692"
query_term = "산업안전보건법"

# 법제처 Open API URL
url = f"http://www.law.go.kr/DRF/lawSearch.do?OC={API_KEY}&target=law&type=XML&query={query_term}"

try:
  response = requests.get(url)
  if response.status_code == 200:
    print("법제처 API 연동 성공!")
    print(response.text[:300])  # 결과 XML 앞부분 출력
  else:
    print(f"API 호출 실패: {response.status_code}")
except Exception as e:
  print(f"오류 발생: {e}")
