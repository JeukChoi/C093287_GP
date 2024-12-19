from flask import Flask, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from googleapiclient.discovery import build
from collections import Counter
import io
import base64
import platform
import matplotlib

matplotlib.use('Agg')

app = Flask(__name__)

API_KEY = 'MY_KEY'
youtube = build('youtube', 'v3', developerKey=API_KEY)

category_map = {
    "1": "Film & Animation", "2": "Autos & Vehicles", "10": "Music",
    "15": "Pets & Animals", "17": "Sports", "18": "Short Movies",
    "19": "Travel & Events", "20": "Gaming", "21": "Videoblogging",
    "22": "People & Blogs", "23": "Comedy", "24": "Entertainment",
    "25": "News & Politics", "26": "Howto & Style", "27": "Education",
    "28": "Science & Technology", "29": "Nonprofits & Activism"
}

def get_trending_videos():
    request = youtube.videos().list(
        part='snippet, statistics',
        chart='mostPopular',
        regionCode='KR',
        maxResults=50
    )
    response = request.execute()
    return response['items']

def extract_video_info(video):
    category_id = video['snippet'].get('categoryId', 'N/A')
    category_name = category_map.get(category_id, 'Unknown')
    return {
        'title': video['snippet']['title'].encode('utf-8').decode('utf-8'),
        'channel': video['snippet']['channelTitle'].encode('utf-8').decode('utf-8'),
        'tags': [tag.encode('utf-8').decode('utf-8') for tag in video['snippet'].get('tags', [])],
        'views': int(video['statistics']['viewCount']),
        'likes': int(video['statistics'].get('likeCount', 0)),
        'comments': int(video['statistics'].get('commentCount', 0)),
        'category': category_name
    }

def generate_charts():
    trending_videos = [extract_video_info(video) for video in get_trending_videos()]
    df = pd.DataFrame(trending_videos)

    charts = []
    
    # 폰트 설정
    if platform.system() == 'Windows':
        font_path = "C:/Windows/Fonts/malgun.ttf"
    elif platform.system() == 'Darwin':  # macOS
        font_path = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    else:  # Linux
        font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
    
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()

    with plt.style.context('default'):
        plt.figure(figsize=(12, 8))
        top_10_views = df.nlargest(10, 'views')
        plt.plot(range(1, 11), top_10_views['views'], marker='o', linestyle='-')
        plt.xticks(range(1, 11), labels=range(1, 11), rotation=0)
        plt.yscale('log')
        plt.title('상위 10개 인기 동영상 조회수', fontproperties=font_prop)
        plt.xlabel('영상 번호', fontproperties=font_prop)
        plt.ylabel('조회수 (로그 스케일)', fontproperties=font_prop)
        plt.tight_layout()

        # 제목을 표 아래에 추가
        plt.figtext(0.1, -0.2, "\n".join([f"영상{i+1}: {title}" for i, title in enumerate(top_10_views['title'])]), 
                    ha="left", fontsize=10, fontproperties=font_prop)

        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        charts.append(base64.b64encode(img.getvalue()).decode())
        plt.close()
        
        # 카테고리별 동영상 수 파이 차트
        category_counts = df['category'].value_counts()
        plt.figure(figsize=(10, 6))
        plt.pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%')
        plt.title('카테고리별 동영상 수', fontproperties=font_prop)
        plt.axis('equal')
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        charts.append(base64.b64encode(img.getvalue()).decode())
        plt.close()

        # 가장 많이 사용된 태그 40개 바 그래프
        all_tags = [tag for tags in df['tags'] for tag in tags]
        most_common_tags = Counter(all_tags).most_common(40)
        tags, counts = zip(*most_common_tags)
        
        plt.figure(figsize=(14, 7))
        plt.bar(tags, counts)
        plt.title('상위 40개 가장 많이 사용된 태그', fontproperties=font_prop)
        plt.xlabel('태그', fontproperties=font_prop)
        plt.ylabel('빈도', fontproperties=font_prop)
        plt.xticks(rotation=45, ha='right', fontproperties=font_prop)
        plt.tight_layout()
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        charts.append(base64.b64encode(img.getvalue()).decode())
        plt.close()
        
        # 동영상 별 좋아요 수와 댓글 수 비교 그래프
        plt.figure(figsize=(12, 6))
        x = range(len(df))
        plt.bar(x, df['likes'], width=0.4, label='좋아요', align='center')
        plt.bar(x, df['comments'], width=0.4, label='댓글', align='edge')
        plt.title('인기 동영상의 좋아요 수와 댓글 수 비교', fontproperties=font_prop)
        plt.yscale('log')
        plt.xlabel('동영상 인덱스', fontproperties=font_prop)
        plt.ylabel('개수 (로그 스케일)', fontproperties=font_prop)
        plt.xticks(x, df['channel'], rotation=90, fontproperties=font_prop)
        plt.legend(prop=font_prop)
        plt.tight_layout()
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        charts.append(base64.b64encode(img.getvalue()).decode())
        plt.close()
    
    return charts

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    try:
        charts = generate_charts()
        data = {'charts': charts}
        return jsonify(data)
    except Exception as e:
        app.logger.error(f"Error generating charts: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
