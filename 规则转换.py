import os
import json

def convert_list_to_json(input_file):
    output_file = os.path.splitext(input_file)[0] + ".json"

    domain_suffix = []
    domain_keyword = []
    domain = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith("DOMAIN-SUFFIX,"):
                domain_suffix.append(line.split(",", 1)[1].strip())
            elif line.startswith("DOMAIN-KEYWORD,"):
                domain_keyword.append(line.split(",", 1)[1].strip())
            elif line.startswith("DOMAIN,"):
                domain.append(line.split(",", 1)[1].strip())

    rules = []
    if domain_suffix:
        rules.append({"domain_suffix": domain_suffix})
    if domain_keyword:
        rules.append({"domain_keyword": domain_keyword})
    if domain:
        rules.append({"domain": domain})

    if not rules:
        print(f"⚠️ 跳过空规则文件: {input_file}")
        return

    data = {        
        "rules": rules,
        "version": 2
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ 已生成: {output_file}")


if __name__ == "__main__":
    for file in os.listdir("."):
        if file.lower().endswith(".list"):
            convert_list_to_json(file)
