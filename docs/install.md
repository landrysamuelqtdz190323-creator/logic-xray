# 安装与第一次使用

文档核对日期：2026-10-02。安装包包含 Skill 指令、六份参考资料和许可；Codex 包另有 UI 元数据。没有模型、运行时抓取脚本或账号连接器。实际宿主导入与输出行为见 [验证记录](validation.md)。

## 选对安装包

| 平台 | 下载 | ZIP 内结构 |
| --- | --- | --- |
| Codex | [reasoned-lens-codex-1.0.0.zip](../dist/reasoned-lens-codex-1.0.0.zip) | `reasoned-lens/SKILL.md`、`agents/`、`references/`、许可 |
| WorkBuddy | [reasoned-lens-workbuddy-1.0.0.zip](../dist/reasoned-lens-workbuddy-1.0.0.zip) | 根目录 `SKILL.md`、`references/`、许可及双语字段 |

整个仓库 ZIP 用于阅读和维护，不能代替 WorkBuddy 专用包。校验值见 [SHA256SUMS](../dist/SHA256SUMS)。

## Codex

解压 Codex 包，保留完整的 `reasoned-lens` 文件夹。

- 只在某个项目使用：复制到项目的 `.agents/skills/reasoned-lens/`。
- 多个项目使用：复制到个人目录 `~/.agents/skills/reasoned-lens/`。Windows 本地环境通常对应 `%USERPROFILE%\.agents\skills\reasoned-lens\`；WSL 使用运行 Codex 的 Linux 用户目录。

若目录不存在，先创建。macOS 可在 Finder 的“前往文件夹”中输入 `~/.agents/skills/`。只复制 `SKILL.md` 会缺少参考资料。

Codex 会发现技能变化；如果没有出现，重启相应项目或 Codex。可明确输入 `$reasoned-lens`，或在技能选择入口选中“看清论证”。不要同时安装多个同名版本。

[OpenAI 官方：本地 Skill 结构与发现位置](https://learn.chatgpt.com/docs/build-skills)

## WorkBuddy

进入“专家·技能·连接器 → 技能”或当前版本的技能入口，选择“添加技能 → 上传技能”，导入 WorkBuddy 专用 ZIP。确认列表出现“看清论证”并启用，然后在新对话中选择它或明确要求使用该技能。

界面入口可能随版本变化；若当前版本没有本地导入入口，应以官方说明为准。包已包含官方要求的双语描述、版本和作者字段，不能把文件校验当作实际导入成功。

[WorkBuddy 官方：技能结构与字段](https://open.workbuddy.cn/docs/skill) · [客户端技能管理](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)

## 第一次试用

使用一个虚构事件，避免先上传私密内容：

```text
请使用 reasoned-lens 分析：
正文 P1：采访的 10 位成功创业者都每天早起，所以早起的人一定会创业成功。
评论 C1，回复 P1：质疑的人就是懒。
材料为虚构，只做材料内分析，不联网，不发布。
请提出两条对应原话、可回答的反问。
```

应区分样本与普遍保证，识别 C1 没有补充证据，说明外部事实未核实；问题应允许补充数据后改变判断。也可用 [案例与报告模板](../references/examples.md) 检查输出。

## 更新与停用

记录版本并保留需要的旧包，在同一安装范围替换或重新导入；确认只启用一个同名技能。停用使用宿主技能开关，手动移除时仅移除自己安装的 `reasoned-lens` 文件夹，不修改其他技能或宿主配置。

## 输入前

删除无关账号、电话和私人联系方式。Skill 没有存储和自动发布程序，但宿主模型可能处理输入，并可能使用用户授权的工具；本地安装不表示推理完全离线。
