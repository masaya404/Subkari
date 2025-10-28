import shutil
import os

# --- 設定 ---

# 1. 元のファイルパス (このファイルは変更されません)
source_file_path = 'image 51.png'

# 2. 保存先のディレクトリ
destination_dir = ''

# 3. ループの範囲
product_id_start = 1
product_id_end = 3   # test01 から test03 まで

sequence_start = 1
sequence_end = 3     # _01 から _03 まで

# --- ここから処理 ---

print(f"処理を開始します...")
print(f"元ファイル: {source_file_path}")

try:
    # 1. 保存先ディレクトリが存在しない場合は作成する
    os.makedirs(destination_dir, exist_ok=True)
    
    copied_count = 0
    
    # 2. 商品IDのループ (1, 2, 3 が順番に入る)
    for pid in range(product_id_start, product_id_end + 1):
        
        # 3. 連番のループ (1, 2, 3 が順番に入る)
        for seq in range(sequence_start, sequence_end + 1):
            
            # 4. ★新しいファイル名を指定のフォーマットで生成
            #    f"test{pid:02d}" -> "test" + 2桁ゼロ埋めのID (例: test01)
            #    f"{seq:02d}"    -> 2桁ゼロ埋めの連番 (例: 01)
            new_filename = f"test{pid:02d}_{seq:02d}.png"
            
            # 5. 保存先のフルパスを生成 (例: img/test01_01.png)
            destination_file_path = os.path.join(destination_dir, new_filename)
            
            # 6. ファイルをコピー
            shutil.copy(source_file_path, destination_file_path)
            
            print(f"  -> {destination_file_path} にコピーしました。")
            copied_count += 1

    print(f"\n処理が完了しました。")
    print(f"合計 {copied_count} 個のファイルをコピーしました。")

except FileNotFoundError:
    print(f"\nエラー: 元のファイルが見つかりません: {source_file_path}")
except Exception as e:
    print(f"\nエラーが発生しました: {e}")