#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sandboxie-Plus 中文翻译优化脚本 - 执行版本
对 sandman_zh_CN.ts 文件进行实际修改
"""

import re

def optimize_file(filepath):
    """读取文件并应用所有优化"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_count = 0
    
    # 定义替换规则 (按优先级排序)
    replacements = [
        # === 术语统一 ===
        # Certificate -> 证书 (不是许可证)
        ("赞助者许可证", "赞助者证书"),
        ("试用许可证", "试用证书"),
        ("免费试用许可证", "免费试用证书"),
        ("评估许可证", "评估证书"),
        ("高级加密功能许可证", "高级加密功能证书"),
        
        # === 精简表达 ===
        # 移除冗余词汇
        ("是否要删除", "是否删除"),
        ("是否要安装", "是否安装"),
        ("是否要更新", "是否更新"),
        ("是否要进行", "是否"),
        ("是否想要", "是否"),
        ("您是否想要", "您是否"),
        ("您是否要", "您是否"),
        
        # 移除冗余的"进行"
        ("进行有限时间的试用", "进行限时试用"),
        ("进行更新", "更新"),
        ("进行编辑", "编辑"),
        ("进行配置", "配置"),
        ("进行选择", "选择"),
        ("进行删除", "删除"),
        ("进行安装", "安装"),
        
        # === 语序和表达优化 ===
        ("将被禁用", "将禁用"),
        ("将被终止", "将终止"),
        ("被终止", "终止"),
        ("被禁用", "禁用"),
        
        # === 标点符号修正 ===
        # 移除问号前多余空格
        (" %1？", " %1?"),
        ("它？", "它?"),
        ("吗？", "吗?"),
        
        # === 具体句子优化 ===
        ("若进行调试，则需要 V4 Script Debugger 插件的调试脚本，是否要下载并安装它？",
         "若要调试故障排除脚本，需要 V4 Script Debugger 加载项，是否下载并安装？"),
        
        ("双击它进行编辑即可", "双击它编辑即可"),
        
        ("你的许可证在当前版本中将保持有效", "该许可证在当前版本中仍有效"),
        
        ("但当您进行更新后", "但更新后"),
        
        ("您确定要进行更新吗？", "您确定要更新吗？"),
        
        ("您确定要更新吗？", "是否继续更新？"),
        
        ("赞助者独占功能将被禁用", "赞助者专属功能将禁用"),
        
        ("对该版本沙盒无效", "对此版本无效"),
        
        ("请获取可用的新许可证", "请获取新证书"),
        
        ("将在 %1 天后过期", "将于 %1 天后过期"),
    ]
    
    # 应用所有替换
    for old, new in replacements:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changes_count += count
            if count > 0:
                print(f"替换 '{old}' -> '{new}': {count} 处")
    
    # 特殊处理：多行文本中的优化
    content = re.sub(r'然后双击它进行编辑即可', r'然后双击它编辑即可', content)
    
    # 保存修改后的文件
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n已保存修改，共 {changes_count} 处改进")
    else:
        print("\n没有发现需要修改的内容")
    
    return changes_count

if __name__ == "__main__":
    filepath = "/workspace/SandboxiePlus/SandMan/sandman_zh_CN.ts"
    print("=" * 60)
    print("开始优化翻译文件...")
    print("=" * 60)
    count = optimize_file(filepath)
    print("=" * 60)
    print(f"优化完成！共改进 {count} 处")
