import os
import hashlib
import json
import argparse

def calc_md5(file_path, chunk_size=8192):
    """计算文件的 MD5 值"""
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()

def should_include(filename, include_exts, exclude_patterns):
    """判断文件是否需要被包含"""
    name_lower = filename.lower()

    # 排除匹配的文件名或扩展名
    for pattern in exclude_patterns:
        if name_lower.endswith(pattern) or pattern in name_lower:
            return False

    # 如果指定了 include 扩展名，则只包含这些
    if include_exts:
        return any(name_lower.endswith(ext) for ext in include_exts)

    return True  # 默认包含所有

def traverse_and_hash(root_dir, include_exts=None, exclude_patterns=None):
    """遍历目录并返回文件信息"""
    results = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if not should_include(filename, include_exts, exclude_patterns):
                continue

            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, root_dir)
            md5_value = calc_md5(full_path)
            results.append({
                "name": rel_path.replace("\\", "/"),
                "md5": md5_value
            })
    return results

def main():
    parser = argparse.ArgumentParser(description="生成目录下所有文件的 MD5 JSON 文件")
    parser.add_argument("directory", help="目标文件夹路径")
    parser.add_argument("-o", "--output", default="../font_list.json", help="输出的 JSON 文件名 (默认: font_list.json)")
    parser.add_argument("--include", help="只包含指定扩展名，如: .ttf,.otf,.txt")
    parser.add_argument("--exclude", help="排除指定文件名或扩展名，如: .txt,OFL.txt")
    args = parser.parse_args()

    target_dir = os.path.abspath(args.directory)
    if not os.path.isdir(target_dir):
        print(f" 目录不存在: {target_dir}")
        return

    include_exts = [e.strip().lower() for e in args.include.split(",")] if args.include else []
    exclude_patterns = [e.strip().lower() for e in args.exclude.split(",")] if args.exclude else []

    print(f"📂 正在扫描目录: {target_dir}")
    if include_exts:
        print(f"   ✅ 仅包含扩展名: {include_exts}")
    if exclude_patterns:
        print(f"   🚫 排除文件: {exclude_patterns}")

    file_list = traverse_and_hash(target_dir, include_exts, exclude_patterns)
    print(f"✅ 共发现 {len(file_list)} 个文件")

    output_path = os.path.join(target_dir, args.output)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(file_list, f, ensure_ascii=False, indent=2)


    print(f"💾 已生成 JSON 文件: {output_path}")

if __name__ == "__main__":
    main()
