import os 

# 폴더명 변경 함수
def change_folder_name(directory):
    # 디렉터리에 있는 모든 폴더를 반복적으로 탐색
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        # 현재 항목이 폴더인지 확인
        if os.path.isdir(folder_path):
            
            # 조건에 따른 폴더명 변경
            if '조건1':
                new_folder_name = '변경할 폴더명' # f''
            elif '조건2':
                new_folder_name = '변경할 폴더명'
            else:
                new_folder_name = '변경할 폴더명'

            # 폴더 이름 변경
                new_folder_path = os.path.join(directory, new_folder_name)
                os.rename(folder_path, new_folder_path)
                print(f"Renamed: {folder_path} -> {new_folder_path}")


# 파일명 변경 함수
def change_file_name(directory):
    # 폴더 내 파일 목록 가져오기
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # 파일명을 이름순으로 정렬
    files.sort()
    
    # 파일 이름 변경
    for index, file_name in enumerate(files):
        # 새 파일명 생성 
        new_file_name = '변경할 파일명명'
        
        # 기존 파일 경로 및 새 파일 경로 생성
        old_file_path = os.path.join(directory, file_name)

        # 기존 파일 확장자 유지
        file_extension = os.path.splitext(file_name)[1]  
        new_file_path = os.path.join(directory, f"{new_file_name}{file_extension}")
        
        # 파일명 변경
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {file_name} -> {new_file_name}{file_extension}")
