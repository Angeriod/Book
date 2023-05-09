import os
import sox

if __name__ ==" __main__":
    original_wav_dir = './data/original/just_ver1.1/repeat500/wav/'

    out_wav_dir = './wav'
    # repeat500 내에서 사용할 세트 수
    num_set =5 
    # repeat500 내에서 사용할 세트 당 발화 수
    num_utt_per_set = 10

    os.makedirs(out_wav_dir, exist_ok=True)
    # sox로 음성 변환 클래스 호출
    tfm = sox.Transformer()
    # 샘플링 주파수를 16000Hz로 변환하도록 설정
    tfm.convert(samplerate=16000)
    #세트 x 발화 몇 분만 처리 실행
    for set_id in range(num_set):
        for utt_id in range(num_utt_per_set):
            # wav 파일 이름
            filename = 'REPEAT500set%d_%03d' % (set_id+1, utt_id+1)
            # 변환 소스의 원본 데이터 (48000Hz) 파일 이름
            wav_path_in = os.path.join(original_wav_dir, filename+'.wav')

            wav_path_out = os.path.join(out_wav_dir, filename+'.wav')

            print(wav_path_in)

            if not os.path.exists(wav_path_in):
                print("Error: Not found %s" % (wav_path_in))
                exit()

            tfm.build_file(input_filepath=wav_path_in, output_filepath = wav_path_out)
