import os

# 프로젝트 폴더 생성 및 디렉토리 구조 설정
os.makedirs('templates', exist_ok=True)
os.makedirs('static', exist_ok=True)

# 확인
print(os.listdir('.'))  # ['templates', 'static'] 출력

html_content = '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>유튜브 트렌드 분석기</title>
    <link rel="stylesheet" href="/static/styles.css">
    <style>
        body {
            display: flex;
            margin: 0;
            font-family: Arial, sans-serif;
            height: 100vh;
            overflow: hidden;
        }
        .menu {
            width: 200px;
            background-color: #f4f4f4;
            padding: 10px;
            box-shadow: 2px 0 5px rgba(0,0,0,0.1);
            position: fixed;
            height: 100vh;
        }
        .menu a {
            display: block;
            padding: 8px;
            text-decoration: none;
            color: #333;
            margin-bottom: 5px;
        }
        .menu a:hover {
            background-color: #ddd;
        }
        .content {
            flex-grow: 1;
            padding: 20px;
            margin-left: 220px;
            overflow-y: auto;
            height: 100vh;
        }
        h1 {
            margin-top: 0;
        }
        @media (max-width: 768px) {
            body {
                flex-direction: column;
                height: auto;
                overflow: auto;
            }
            .menu {
                width: 100%;
                height: auto;
                position: fixed;
                top: 0;
                display: flex;
                justify-content: space-around;
                box-shadow: none;
                border-bottom: 1px solid #ccc;
                z-index: 1000;
            }
            .content {
                margin-left: 0;
                padding-top: 60px;
                height: auto;
                overflow-y: auto;
                flex-grow: 1;
            }
        }
    </style>
</head>
<body>
    <div class="menu">
        <a href="#" class="menu-link" data-section="section1">내 채널 분석하기</a>
        <a href="#" class="menu-link" data-section="section2">인기급상승동영상 트렌드 분석 레포트</a>
        <a href="#" class="menu-link" data-section="section3">기능 3</a>
        <a href="#" class="menu-link" data-section="section4">기능 4</a>
    </div>
    <div class="content">
        <h1 id="title">원하는 기능을 선택하시오</h1>
        <p id="content"></p>
    </div>

    <script>
    document.querySelectorAll('.menu-link').forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const sectionId = this.getAttribute('data-section');
            updateContent(sectionId);
        });
    });

    function updateContent(section) {
        const content = document.getElementById('content');
        const title = document.getElementById('title');
        content.innerHTML = '<p>로딩 중...</p>'; // 로딩 표시 추가

        if (section === 'section1') {
            title.textContent = '내 채널 분석하기';
            content.innerHTML = '<strong>내 채널 분석 기능 준비중</strong>';
        } else if (section === 'section2') {
            title.textContent = '인기급상승동영상 트렌드 분석 레포트';
            fetch('/api/data')
                .then(response => response.json())
                .then(data => {
                    content.innerHTML = data.charts.map((chart, index) => 
                        `<div>
                            <h2>차트 ${index + 1}</h2>
                            <img src="data:image/png;base64,${chart}" alt="Chart ${index + 1}" style="max-width: 100%;">
                        </div>`
                    ).join('');
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    content.innerHTML = '<p>데이터를 불러오는 중 오류가 발생했습니다.</p>';
                });
        } else if (section === 'section3') {
            title.textContent = '기능3 타이틀';
            content.textContent = '기능3 내용';
        } else if (section === 'section4') {
            title.textContent = '기능4 타이틀';
            content.textContent = '기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 기능4 내용 ';
        }
    }
</script>
</body>
</html>'''

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

css_content = '''
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}
h1 {
    color: #333;
}
'''

with open('static/styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

scripts_content = '''
console.log('Flask 애플리케이션 로드됨');
'''

with open('static/scripts.js', 'w', encoding='utf-8') as f:
    f.write(scripts_content)
