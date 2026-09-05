#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sandboxie-Plus 中文翻译优化脚本
改进目标：
1. 术语统一（沙盒/主机/宿主、映像、模板、赞助者/许可证等）
2. 精简冗长的翻译
3. 调整不自然的语序
4. 修正标点符号问题
"""

import re
import sys

# 术语映射表 (英文 -> 推荐中文)
TERM_MAP = {
    # Box 相关 - 统一为"沙盒"
    "sandbox": "沙盒",
    "box": "沙盒",
    
    # Host 相关 - 统一为"主机"
    "host": "主机",
    "hosts": "主机",
    
    # Image 相关 - 统一为"映像"
    "image": "映像",
    "disk image": "磁盘映像",
    
    # Template 相关 - 统一为"模板"
    "template": "模板",
    
    # Certificate 相关 - 统一为"证书"
    "certificate": "证书",
    "supporter certificate": "赞助者证书",
    
    # Add-on 相关 - 统一为"加载项"
    "add-on": "加载项",
    "addon": "加载项",
}

# 需要优化的翻译模式 (正则匹配 -> 替换函数)
OPTIMIZATION_PATTERNS = [
    # 1. 移除多余的空格
    (r'\s+([,.!?.])', r'\g<1>'),  # 标点前多余空格
    (r'([,.!?])\s{2,}', r'\g<1> '),  # 标点后多余空格
    
    # 2. 统一术语
    ("赞助者许可证", "赞助者证书"),  # certificate 应该是证书
    ("试用许可证", "试用证书"),
    ("免费试用许可证", "免费试用证书"),
    ("评估许可证", "评估证书"),
    ("高级加密功能许可证", "高级加密功能证书"),
    
    # 3. 精简表达
    ("是否要", "是否"),
    ("是否想要", "是否"),
    ("你想要", "您要"),
    ("你想要", "您要"),
    
    # 4. 调整语序 - 被动改主动
    ("被阻止", "无法"),
    ("被禁用", "已禁用"),
    ("被启用", "已启用"),
    
    # 5. 简化冗余表达
    ("进行配置", "配置"),
    ("进行编辑", "编辑"),
    ("进行选择", "选择"),
    ("进行删除", "删除"),
    ("进行安装", "安装"),
    ("进行更新", "更新"),
    
    # 6. 统一标点
    (" ！", "!"),
    (" ？", "?"),
    (" ,", ","),
    (" .", "."),
]

def optimize_translation(text):
    """优化单条翻译"""
    result = text
    
    for pattern, replacement in OPTIMIZATION_PATTERNS:
        if callable(replacement):
            result = re.sub(pattern, replacement, result)
        else:
            result = result.replace(pattern, replacement)
    
    return result

def analyze_ts_file(filepath):
    """分析 TS 文件并返回统计信息"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 统计各类翻译状态
    translations = re.findall(r'<translation[^>]*>(.*?)</translation>', content, re.DOTALL)
    unfinished = len(re.findall(r'type="unfinished"', content))
    obsolete = len(re.findall(r'type="obsolete"', content))
    vanished = len(re.findall(r'type="vanished"', content))
    normal = len(translations) - unfinished - obsolete - vanished
    
    print(f"文件分析: {filepath}")
    print(f"  总翻译数：{len(translations)}")
    print(f"  正常翻译：{normal}")
    print(f"  未完成：{unfinished}")
    print(f"  已废弃 (obsolete): {obsolete}")
    print(f"  已消失 (vanished): {vanished}")
    print()
    
    return {
        'total': len(translations),
        'normal': normal,
        'unfinished': unfinished,
        'obsolete': obsolete,
        'vanished': vanished
    }

def main():
    filepath = "/workspace/SandboxiePlus/SandMan/sandman_zh_CN.ts"
    
    print("=" * 60)
    print("Sandboxie-Plus 中文翻译优化分析")
    print("=" * 60)
    print()
    
    # 分析文件
    stats = analyze_ts_file(filepath)
    
    # 读取文件内容
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找出可以优化的翻译
    print("可优化的翻译示例:")
    print("-" * 60)
    
    translation_pattern = re.compile(
        r'<source>([^<]+)</source>\s*\n\s*<translation>([^<]+)</translation>',
        re.MULTILINE
    )
    
    improvements = []
    for match in translation_pattern.finditer(content):
        source = match.group(1)
        translation = match.group(2)
        
        optimized = optimize_translation(translation)
        if optimized != translation:
            improvements.append((source, translation, optimized))
            if len(improvements) <= 20:  # 只显示前 20 个
                print(f"原文：{source}")
                print(f"当前：{translation}")
                print(f"建议：{optimized}")
                print()
    
    print(f"\n共发现 {len(improvements)} 处可优化的翻译")
    print("\n主要改进建议:")
    print("1. 术语统一：将'许可证'改为'证书'(certificate)")
    print("2. 精简表达：移除冗余的'进行'、'想要'等词")
    print("3. 语序调整：被动语态改为主动语态")
    print("4. 标点规范：统一中英文标点使用")

if __name__ == "__main__":
    main()
