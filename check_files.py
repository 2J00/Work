import os
import json

# 데이터 중복 확인 코드
def check_duplicate(data):
    # 중복 데이터 확인인
    dup = data.duplicated('중복 확인할 열', keep = ['first'/'last'])
    print(f'중복 데이터 개수: {dup.sum()}')

    # 중복 데이터 제거
    data = data.drop_duplicates('중복 제거가 필요한 열', keep = ['first'/'last'])
    print(f'중복 제거 후 데이터 개수: {data.shape}')


# 잘못 라벨링한 데이터 코드
def check_json_label(directory):
    # 라벨링이 잘못된 데이터를 저장할 리스트 생성
    labeling_error = []

    # 디렉토리 내 파일 순회
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('파일형식 ex) .json'):
                file_path = os.path.join(root, filename)
                folder = os.path.basename(root)
                Label = '[정확한 라벨 이름]'

                try:
                    # json 파일 열기
                    with open(file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)

                        # json 파일 내 label 확인
                        for shape in data.get('shapes', []):
                            json_label = shape.get('label', None)
                            # 라벨 값 비교
                            if json_label != Label:
                                labeling_error.append(file_path)
                
                except KeyError:
                    print(f"라벨 키 오류 발생: {file_path}, Label: {Label}")
                except json.JSONDecodeError:
                    print(f"JSON 파일 읽기 오류: {file_path}")
                except Exception as e:
                    print(f"알 수 없는 오류 발생: {file_path}, {e}")
    
    print(f"라벨링 오류가 발생한 파일: {labeling_error}")
    

# 파일 개수 확인 코드
def count_files(directory):
    cnt_1 = 0 # 파일형식1 개수 저장할 변수 ex) cnt_img
    cnt_2 = 0 # 파일형식2 개수 저장할 변수 ex) cnt_json

    for root, dirs, files in os.walk(directory):
        folder = os.path.basename(root)
        
        for filename in files:
            if filename.endswith('파일형식1 ex) .img'):
                cnt_1 += 1
            if filename.endswith('파일형식2 ex) .json'):
                cnt_2 += 1
                
    print(f"파일형식1 개수: {cnt_1}")
    print(f"파일형식2 개수: {cnt_2}")