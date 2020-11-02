



### Error 01

<img src="README.assets/image-20201102133345447.png" alt="image-20201102133345447"  />

프로젝트 내에서 `settings.py` 파일을 찾을 수 없음 ➡ 파일 구조 확인 결과 settings.py 파일이 프로젝트 폴더 외부에 있었으므로 폴더 이름 변경 및 파일 이동 후 성공

### Error 02

**BE** 로그아웃 후 이동되는 페이지 url이 메인 페이지`path('', blog**.**views**.**home, name='home')`이 아니라 logout url로 따로 이동되는 것 수정 필요.

![image-20201102143042091](README.assets/image-20201102143042091.png)

### Error 03

![image-20201102144035693](README.assets/image-20201102144035693.png)

**FE** 기숙사 소개 페이지 한 화면에 출력될 수 있도록 수정하기(스크롤바 사용 ❌)

### Error 04

매칭용 설문조사 제출 후에 뜨는 화면.

매칭하는 게 일인 웹인데 매칭을 못하면 아 어쩌란 말이냐

![image-20201102152137313](Errors.assets/image-20201102152137313.png)

>  `matching query does not exist`는 주로 `object.get`가 정보를 찾지 못했을 때 발생한다

