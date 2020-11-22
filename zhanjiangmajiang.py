import requests
import re
url = "http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc"
headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",                
        "Cookie": "XSRF-TOKEN=eyJpdiI6InFXbUQ1T3Z0N1RwcU56Nnc0RHY5SGc9PSIsInZhbHVlIjoiYTdlWnZnSUhHN0k0YWxiWnI3VWJHczlpK0NcL1Bnd1F0RU80YkZDczc4SXRKZTczZFdFb0NYeU1TaFZFQ2RTRE0iLCJtYWMiOiI3YWZlMTU4NTkyMjA2MmYyMmQ0MTQ3NDA3NmQ4YjIzYjBhNGNhZWZkYzE5Y2M0YWE3MGZlODYwZDRlZDFkMDVjIn0%3D; szxx_session=eyJpdiI6IkdlaTFpaU40akRqKzVlOGtleFRtQkE9PSIsInZhbHVlIjoiR1VFUDFXSEdpVkFwWkVBNzBrR0tOcU9hb01mUXk4UGxOcmhZYVJCQWxTXC9wOGk1Z1Y1SGFjV0QrUFJrcmFzNTEiLCJtYWMiOiIxNTEwMDc3OTRhYWU0YjMyZmFhNmQxMmY5MTQzMzJmMzk5N2RmZTg3MDlmN2NiNzg1ZGE4MjdhNzZkMzNhZWU3In0%3D",
        
}
res = requests.get(url,headers=headers)
print(res.status_code)
try:
    
    print(res.text)
    result = re.findall("var _CSRF = '(.*?)';",res.text)
    # print("result",result[0])
except Exception as e :
    print(e)
    # print(res.headers.get("Set-Cookie"))
    print("something went wrong")
else:  
    print("Token_Get ",result[0])
    # print("Set-Cookie",res.headers.get("Set-Cookie"))
    # 手动获得cookie
    cookies = res.headers.get("Set-Cookie").replace("httponly,","").split(";")
    # print(cookies[0]+";"+cookies[4])
    api_headers = {        
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",       
        "Cookie":cookies[0]+";"+cookies[4],              
        "X-CSRF-TOKEN": result[0],
    }
    api_url = "http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList"
    data = {
        "offset": 0,
        "limit": 20,
        "site_id": 759010
    }
    api_res = requests.post(api_url,data=data,headers=api_headers)
    print(api_res.json())
 