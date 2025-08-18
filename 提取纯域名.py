import os

# 当前文件夹
current_folder = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(current_folder):
    if filename.endswith(".list"):
        input_path = os.path.join(current_folder, filename)
        output_path = os.path.join(current_folder, os.path.splitext(filename)[0] + ".txt")

        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            # 删除指定字符串
            stripped = stripped.replace("DOMAIN,", "").replace("DOMAIN-SUFFIX,", "").strip()
            if stripped:
                new_lines.append(stripped)

        # 写入文件，保证最后没有空行
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))

        print(f"已处理: {filename} -> {os.path.basename(output_path)}")


#python 提取纯域名.py
