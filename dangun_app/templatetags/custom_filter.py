from django import template
from bs4 import BeautifulSoup
import re


register = template.Library()

# 글 미리보기 기능
@register.filter
def text_only(value):
    soup = BeautifulSoup(value, "html.parser")

    # img 태그 제거
    for img in soup.find_all('img'):
        img.decompose()
    
    # 텍스트만 추출, 첫 20글자만 반환
    text_content = soup.get_text()
    if len(text_content) >= 200:
        text_content = text_content[:200] + '...'
    return text_content



# 첫 번째 img 태그의 src 속성 값 찾아 반환함
@register.filter(name='get_img_src')
def get_img_src(value):
    match = re.search(r'<img [^>]*src="([^"]+)', value)
    if match:
        return match.group(1)
    return ''