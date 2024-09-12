########################################
# pip install wordcloud
# pip list
########################################
# 워드클라우드 라이브러리 설치
# 문자의 사용빈도에 따라 글자의 크기를 조절 하여 보여주는 라이브러리
import os

from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
# d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
# text = open(path.join(d, 'constitution.txt')).read()
f = open('ex/2. 게티즈버그_한글.txt', 'r', encoding='utf-8')
text = f.read()


# Generate a word cloud image
# font_path : 한글이 깨지는것을 방지 하기 위해 한글폰트의 경로를 지정
wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf').generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")     # 축을제거
plt.show()          # 창을 띄워줌

# lower max_font_size  <== 최대폰트 크기를 지정
# wordcloud = WordCloud(max_font_size=40).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()