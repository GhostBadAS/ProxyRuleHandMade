import os
import codecs

# 输入 / 输出目录
INPUT_DIR = "."
OUTPUT_DIR = "mihomo"

# 创建 clean 目录
os.makedirs(OUTPUT_DIR, exist_ok=True)

def is_comment(line: str) -> bool:
    return line.startswith("#") or line.startswith("//")

def clean_lines(lines):
    cleaned = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if is_comment(line):
            continue
        cleaned.append(line)
    return cleaned

def main():
    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(".list"):
            continue

        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        try:
            # utf-8-sig 自动去 BOM
            with codecs.open(input_path, "r", "utf-8-sig") as f:
                lines = f.readlines()

            cleaned = clean_lines(lines)

            if not cleaned:
                print(f"[跳过] {filename}（清洗后为空）")
                continue

            with open(output_path, "w", encoding="utf-8") as f:
                f.write("\n".join(cleaned))

            print(f"[OK] {filename} → clean/{filename}")

        except Exception as e:
            print(f"[错误] {filename}: {e}")

if __name__ == "__main__":
    main()
