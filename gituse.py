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
git add . git add use.py use2.py 로 지정해서 업데이트가 가능하다
git commit -m "커밋 내용"
git push origin branch이름

브랜치는 master 브랜치에서 develop 브랜치로 분기한다.
개발자는 develop 브랜치에서 자유롭게 커밋 혹시나 feature에 개별 기능이 존재할 경우 feature를 통해 develop로 커밋 
배포전에 QA용으로 만드는 브랜치로 release


브랜치 로컬에 로컬로 저장하기
git stash -> 수정한 내용이 사라지고 저장됨
git stash list -> 저장된 목록 확인
git stash pop -> 다시 꺼내오기
git stash apply 적용은 하되 목록에서 삭제는 안함
git stash drop "stash@{0}" 특정 stash 삭제
git stash clear 전체 삭제

  asdf
# 내 브랜치(현재 브랜치) 내용으로 유지??
git checkout --ours gituse.py

# 상대방(merge해오는 쪽) 내용으로 유지??
git checkout --theirs gituse.py

merge 중이면 ESC -> :wq로 초기화


```
"""
