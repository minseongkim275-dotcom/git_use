"""
git clone <템플릿-저장소-URL>
cd [git clone으로 저장한 폴더 주소]
rm -rf .git #숨겨진 깃 파일 삭제하기
git init    #새로운 저장소로 초기화
git remote add origin <본인-저장소-URL> # remote는 주소록에 연락처를 등록하는 것 
git set-url은 주소변경
git add .
git commit -m "Initial commit"
git branch -M main


git push -u origin main

-u 없이: 매번 "누구한테 보낼지" 주소를 다 써야 하는 것
-u 있으면: 한 번 "기본 수신자"로 등록해두고, 다음부턴 이름만 눌러도 보내지는 것


git remote add origin (url주소)
git install -r requirements.txt


- 가상환경 설정


- 가상환경
python -m venv venv
venv\Scripts\activate
deactivate

 PR(Pull Request) 과정
git clone -b (브랜치 이름) (url)
git branch [현재 사용중인 브랜치] -> 브랜치 이동은 git checkout [해당 브랜치 이름] -> git switch -c "브랜치 이름"
git branch -d feature/login # 로컬 브랜치 삭제 git push origin --delete feature/login 원격 브랜치 삭제
git add . git add use.py use2.py 로 지정해서 업데이트가 가능하다
git commit -m "커밋 내용"
git push origin branch이름

브랜치는 master 브랜치에서 develop 브랜치로 분기한다.
개발자는 develop 브랜치에서 자유롭게 커밋 혹시나 feature에 개별 기능이 존재할 경우 feature를 통해 develop로 커밋 
배포전에 QA용으로 만드는 브랜치로 release
같은 브랜치의 경우는 push를 하면 pr이 생기지 않기 때문에
브랜치를 분할해서 사용한다는 뜻은 develop/feature/login 랑 develop/feature/logout 과 같이 주소형식으로 다른 브랜치를 만들어
develop/feature로 pr한다는 것이다. 근데 한번 만든 pr은 다시 merge가 뜨지않는다.?


브랜치 로컬에 로컬로 저장하기
git stash -> 수정한 내용이 사라지고 저장됨
git stash list -> 저장된 목록 확인
git stash pop -> 다시 꺼내오기 번호를 지정하지않을시 가장 최근에 적용한 것이 pop된다. git stash pop "stash@{1}" 시 적용
git stash apply 적용은 하되 목록에서 삭제는 안함
git stash drop "stash@{0}" 특정 stash 삭제
git stash clear 전체 삭제
stash는 최근꺼부터 채워지기 시작해 {0}이 가장최근 가져온 것


# 내 브랜치(현재 브랜치) 내용으로 유지??
git checkout --ours gituse.py

# 상대방(merge해오는 쪽) 내용으로 유지??
git checkout --theirs gituse.py

merge 중이면 ESC -> :wq로 초기화

가상환경에서 먼저 pip로 인스톨을 진행하고 pip freeze > requirements.txt
pip freeze > requirements.txt 를 사용시 현재 사용하는 패키지 버전을 그대로 가져온다.

새 브랜치를 처음 push하면 → GitHub이 "어, 새 브랜치네! main과 비교해서 PR 만들래?"라고 처음 한 번 자동으로 배너를 띄워줌
그 브랜치에 계속 커밋을 추가하고 다시 push해도 → 이미 GitHub이 그 브랜치를 알고 있으니, 배너가 다시 안 뜰 수도 있음 (하지만 PR은 여전히 수동으로 만들 수 있음)
실제로 main에 합쳐지는(merge) 시점은 → push할 때가 아니라, GitHub PR 페이지에서 "Merge" 버튼을 직접 눌렀을 때만 일어남


```
"""
