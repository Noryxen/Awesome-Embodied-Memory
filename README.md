# Awesome Embodied Memory

A curated collection of papers on how embodied agents acquire, represent, reuse, and continually update experience and skills.

本仓库关注广义的**具身记忆（Embodied Memory）**：机器人如何从人类视频和机器人轨迹中获得经验，如何把经验表示为可迁移的动作、技能或程序，如何在新任务中调用这些经验，以及如何在持续学习和失败反馈中更新它们。

## Contents

- [Memory Acquisition from Demonstrations](#memory-acquisition-from-demonstrations)
- [Cross-Embodiment Representation and Transfer](#cross-embodiment-representation-and-transfer)
- [Procedural Memory, Skill Reuse, and Composition](#procedural-memory-skill-reuse-and-composition)
- [Continual Learning and Adaptation](#continual-learning-and-adaptation)
- [Failure-Driven Post-Training](#failure-driven-post-training)

## Memory Acquisition from Demonstrations

将人类视频或既有交互记录变成模型可以学习的监督信号，是具身记忆形成的第一步。这一类工作关注动作标签生成、三维重建、重定向、仿真增强以及人类视频预训练。

- **Ego-Pi: VLA Fine-Tuning for Ego-Centric Human and Robot Data** — *CVPR 2026*  [Paper](https://arxiv.org/abs/2606.08107)
  - **摘要：** Ego-Pi 将第一视角人类示范与灵巧人形机器人的真实轨迹共同用于微调 π0.5，使人类数据传递的不只是手部运动，还包括分类规则、步骤顺序和已有技能的新组合。它通过人手到机器人关节的映射及交错动作表示适配高维双手控制。局限是仍需机器人示范完成低层动作对齐，依赖特定灵巧手映射与联合训练，不能把任意网络视频直接变成可靠动作。

- **VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation** — *CVPR 2025*  [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_VidBot_Learning_Generalizable_3D_Actions_from_In-the-Wild_2D_Human_Videos_CVPR_2025_paper.pdf)  [Code](https://github.com/ethz-mrl/VidBot)
  - **摘要：** VidBot 从野外单目人类视频中学习物体的三维可供性，将“在哪里接触”和“接触后怎样运动”表示为可迁移的三维动作，再用粗到细的生成模型迁移到新物体和新场景，实现无需针对任务再次训练的机械臂操作。局限是三维伪标签、物体分割和轨迹恢复误差会层层传播，方法偏重几何而非力与接触动力学，最终执行仍依赖抓取、规划和控制模块。

- **Do as I Do: Dexterous Manipulation Data from Everyday Human Videos** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2606.19333)  [Code](https://github.com/malik-group/do-as-i-do)
  - **摘要：** 该工作把日常单目 RGB 视频中的手—物交互重建为三维轨迹，再将人手运动重定向到灵巧机器人手，从而把原本没有机器人动作标签的视频转成可执行、可用于训练的机器人数据，并在真机上验证重放效果。它更像一条数据生产管线而非通用策略。局限是依赖手物重建、接触估计和平台特定重定向，遮挡或尺度误差会影响执行，也没有解决技能检索与长期更新。

- **Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2606.08828)
  - **摘要：** Video2Sim2Real 从一段人类操作视频自动构建可交互的数字孪生，提取物体运动与机器人运动先验；再以物体中心关键帧为锚点优化机器人姿态，并结合模仿学习校准感知误差、残差强化学习修正手指接触，最后迁移到真机。贡献是串起视频、仿真、优化、训练和执行的完整链路。局限是管线复杂且每个任务仍需仿真优化与训练，重建质量和 sim-to-real 偏差会限制泛化速度。

- **RoboWheel: A Data Engine from Real-World Human Demonstrations for Cross-Embodiment Robotic Learning** — *CVPR 2026*  [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_RoboWheel_A_Data_Engine_from_Real-World_Human_Demonstrations_for_Cross-Embodiment_CVPR_2026_paper.pdf)
  - **摘要：** RoboWheel 是一套人类视频数据引擎：从单目 RGB 或 RGB-D 视频重建手—物交互，用强化学习优化接触与穿透等物理合理性，再把轨迹重定向到夹爪、灵巧手和人形机器人，并在 Isaac Sim 中做外观、物体和轨迹增强。生成数据可训练多种 VLA 与模仿策略。局限是它提供的是训练数据而非立即可调用的技能，质量受重建、物理优化和重定向共同制约，下游仍需较大训练成本。

- **Robots Acquire Manipulation Skills in Seconds from a Single Human Video** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2607.20033)
  - **摘要：** HOST 让机器人在推理时用一段人类视频快速获得新技能：先估计机器人处于示范流程的哪个进度，再预测符合下一阶段的人形无关未来观测，最后由未来观测推出机器人动作。训练时用共享任务进度流形把人类视频与机器人轨迹对齐，因此测试时无需再更新整个策略。局限是“一次视频学会”依赖预先训练好的跨本体进度与预测模型，其能力边界仍受训练任务分布、视觉对应关系和未来预测误差影响。

- **HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2606.20521)
  - **摘要：** HumanScale 在相同模型、算力、五千小时数据和后训练协议下，对比第一视角人类视频与遥操作机器人数据作为预训练来源，发现人类视频因场景、物体和行为更丰富，对未见任务的泛化更强。人类手部运动先被重定向成机器人兼容的伪动作，之后仍用少量真机数据对齐。局限是结论主要基于特定世界—动作模型和数据筛选流程，伪动作并不精确，能否在更多 VLA、机器人形态和更大规模下保持优势仍待验证。

- **EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2602.16710)
  - **摘要：** EgoScale 用超过 20,854 小时带伪动作标签的第一视角人类视频预训练 VLA，再通过少量对齐的人类—机器人数据进行中间训练，使 22 自由度灵巧手获得长时程操作和单样本任务适应能力，并观察到数据规模与损失之间的对数线性规律。局限是大规模视频仍需可靠的手部估计与动作重定向，最终控制离不开机器人数据对齐；结果集中在相近的手部操作形态，不能直接代表任意跨本体迁移。

## Cross-Embodiment Representation and Transfer

这类工作不一定把人类视频直接翻译成机器人关节动作，而是先寻找人和机器人之间共享的中间表示，例如潜在技能、任务语义、物体轨迹或对齐后的动作空间。

- **UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations** — *CoRL 2025*  [Paper](https://arxiv.org/abs/2505.08787)  [Code](https://github.com/KimHanjung/UniSkill)
  - **摘要：** UniSkill 用无标签的人类与机器人视频训练逆向技能动力学和前向技能动力学，从相隔若干帧的变化中提取与具体身体无关的潜变量 `z`；机器人策略再依据自身观测和 `z` 输出动作，因此训练不要求人机成对、同场景示范。局限是 `z` 是隐式向量而非可读、可直接调用的技能，低层策略仍需带动作的机器人数据训练，效果也依赖视频时间窗口、视觉域和训练分布。

- **Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers** — *RSS 2024*  [Paper](https://arxiv.org/abs/2403.12943)
  - **摘要：** Vid2Robot 是视频条件的端到端策略：输入一段人类任务视频、机器人当前图像和状态，经交叉注意力直接预测机器人动作，并用对比损失对齐人类视频与机器人执行视频的表示。它在真机上展示了跨物体动作迁移和一定的长时组合能力。局限是训练阶段需要大量“提示视频—机器人轨迹”配对，视频没有被直接转换成动作标签；泛化主要来自训练分布中的任务对应关系，也没有显式、可编辑的技能记忆。

- **Vision-based Manipulation from Single Human Video with Open-World Object Graphs** — *Autonomous Robots 2026*  [Paper](https://doi.org/10.1007/s10514-026-10253-8)
  - **摘要：** ORION 从一段 RGB 或 RGB-D 人类视频提取关键物体、交互点、点云轨迹及接触关系，组成 Open-World Object Graph 序列；执行时识别当前物体，将示范的物体中心轨迹变换到新场景，再优化机器人末端的 SE(3) 动作。它无需训练或更新独立策略，并在真机测试跨背景、视角、布局和物体实例。局限是严重依赖开放词汇识别、三维定位与匹配质量，适合可由物体几何轨迹描述的桌面任务，难以表达力控制和复杂灵巧接触。

- **ImMimic: Cross-Domain Imitation from Human Videos via Mapping and Interpolation** — *CoRL 2025 Oral*  [Paper](https://openreview.net/forum?id=7iaYcss56y)  [Code](https://github.com/GaTech-RL2/ImMimic-CoRL2025)
  - **摘要：** ImMimic 先估计并重定向人手轨迹，再用动态时间规整把人类与少量机器人示范对齐，并通过 MixUp 在二者之间生成中间域，最终共同训练扩散策略。它在四种末端执行器和四项真机任务中提高了成功率与运动平滑性。局限是并非零机器人数据方法，必须依赖少量高质量遥操作轨迹作为锚点；手姿估计、时序匹配和插值错误都会进入训练，且生成的是策略监督而非独立技能条目。

## Procedural Memory, Skill Reuse, and Composition

这一组更接近“技能库”概念：把成功经验保存为程序、计划、轨迹示例、原子动作或参数专家，并在后续任务中检索、组合或扩展。

- **ASPIRE: Agentic /Skills Discovery for Robotics** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2607.00272)
  - **摘要：** ASPIRE 采用 Code-as-Policy：智能体生成机器人控制程序，执行后读取多模态轨迹诊断失败，提出修复并验证；成功修复会被提炼为可复用代码技能，进化搜索再主动组合任务、探索更多程序，使技能库持续增长。它覆盖多个模拟基准，并给出跨机器人 API 的初步真机迁移证据。局限是依赖预设控制接口、基础模型生成代码的可靠性与自动验证，真机规模仍小，技能也容易绑定具体软件栈，并不处理人类视频到动作的问题。

- **ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning** — *arXiv 2025*  [Paper](https://arxiv.org/abs/2509.24219)
  - **摘要：** ViReSkill 用视觉反馈弥补 LLM 符号计划与真实几何之间的差距：执行失败后，重规划器依据当前场景生成新的动作序列；一旦成功，就把这段经过验证的计划存进技能记忆，之后遇到相似情形直接复用，减少模型调用并稳定输出。论文在 LIBERO、RLBench 和真机上验证。局限是记忆主要保存高层计划而非端到端低层控制，检索与执行仍依赖感知、基础技能和场景相似性，错误成功判定也可能污染技能库。

- **Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation** — *ICRA 2026*  [Paper](https://arxiv.org/abs/2603.02623)
  - **摘要：** Uni-Skill 从大规模无结构机器人视频中自动切分、描述并按 VerbNet 风格建立层次化 SkillFolder；规划器发现现有技能不足时会请求新技能，再检索语义相近示例和细粒度空间轨迹，推断新技能并扩展仓库。它在仿真与真机上验证组合泛化。局限是主要处理已有 6-DoF 机器人视频而非任意人类视频，自动标注、深度和轨迹恢复误差会影响技能质量，“自演化”更多是离线检索式扩展，缺少长期部署中的版本、冲突和失效管理。

- **InSight: Self-Guided Skill Acquisition via Steerable VLAs** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2606.24884)  [Code](https://github.com/insight-vla/insight)
  - **摘要：** InSight 先利用 VLM、末端速度和边界细化，把示范切成“移动、抬起、倾倒”等可用语言控制的原语，并微调出可被原语指令引导的 VLA；面对新任务时，VLM 找出缺失原语、提出低层控制、在环境中自主尝试和验证，再把成功数据加入训练集重新训练。局限是需要真实或仿真交互来采集新技能，验证器和低层控制可能出错，重训练仍有成本与安全风险，技能主要内化于模型而非完全独立的外部模块。

- **SkillNet: Hierarchical Skill Modeling for Compositional Generalization in Vision-Language Action Models** — *ICML 2026*  [Paper](https://openreview.net/pdf/7c5a1746602e6ac6c6026477a838d2a89c232171.pdf)
  - **摘要：** SkillNet 用 Motion Code 描述动作的机械属性、用 VerbNet 描述语义角色，建立层次技能结构；技能嵌入作为瓶颈控制混合专家路由，使相似或重复技能激活相似专家，从而把学过的局部能力迁移到新任务组合。仿真和真机均展示零样本与少样本提升。局限是需要预定义或标注的技能层次，知识主要存于参数和专家路由中，并非可审计的外部技能库；真正新颖的运动仍需要数据和训练。

## Continual Learning and Adaptation

这一类研究关注机器人依次学习新任务时，怎样增加能力而不破坏旧能力，以及新经验应写入参数、适配器、回放缓存还是快速记忆。

- **AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots** — *CVPR 2026*  [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html)  [Code](https://github.com/zhanglk9/AtomicVLA)
  - **摘要：** AtomicVLA 联合生成任务计划、原子技能与细粒度动作，并用 Skill-Guided Mixture-of-Experts 为抓取、放置、开合等原子技能分配专门专家；学习新技能时增加和路由新专家，以减轻多技能干扰，支持长时程组合与持续学习。局限是原子技能边界和标签主要由既有数据及规划模块提供，新技能仍需大量人类示范和训练；技能库本质上是模型内专家集合，缺少显式验证、版本和跨机器人接口。

- **CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion** — *IEEE RA-L 2026*  [Paper](https://arxiv.org/abs/2601.09512)  [Code](https://github.com/utiasDSL/clare)
  - **摘要：** CLARE 冻结基础 VLA，在部分前馈层加入轻量适配器；学习新任务时根据逐层特征相似度判断复用旧模块还是扩展新模块，部署时由自编码器路由器在没有任务 ID 的情况下选择适配器。它避免保存旧样本，并在 LIBERO 上显著缓解遗忘。局限是每个新任务仍需机器人示范和训练，参数与路由器会随任务增长；实验主要基于相对紧凑的 VLA 与基准任务，复杂开放环境中的错误路由和长期容量仍未解决。

- **PHASER: Phase-Aware and Semantic Experience Replay for Vision-Language-Action Models** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2606.03598)
  - **摘要：** PHASER 指出整条轨迹均匀回放会漏掉短暂但关键的子技能，因此先按操作阶段分配均衡缓存，再结合语言、视觉和动作干扰程度优先回放最容易遗忘的历史阶段；Auto-PC 用动作变化点和 VLM 语义验证自动寻找阶段边界。它在三种 VLA 和 LIBERO 持续学习套件上取得明显提升。局限是主要为仿真实验，核心评估仍较依赖阶段标注或动作信号，回放只能保持已有经验，不能从无动作视频获得新技能。

- **Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning** — *ICML 2026 Oral*  [Paper](https://arxiv.org/abs/2603.03818)  [Code](https://github.com/Continual-VLAs)
  - **摘要：** 这项研究系统比较预训练 VLA 与从头训练的小策略，发现 π0、GR00T 等大模型配合很小的经验回放缓存就能显著减少甚至消除遗忘；即使旧任务成功率下降，少量微调也能快速恢复，说明知识往往仍保留在内部。贡献主要是改变持续学习的经验判断，而非提出复杂新架构。局限是证据集中在 LIBERO 模拟基准，预训练数据和模型规模存在混杂因素，也没有解决人类视频获取、外部技能组织和真实长期部署。

- **Continually Evolving Skill Knowledge in Vision Language Action Model** — *arXiv 2025*  [Paper](https://arxiv.org/abs/2511.18085)
  - **摘要：** Stellar VLA 用潜在任务—技能知识空间组织连续到来的机器人示范，并以知识引导混合专家路由；T-Stellar 建模任务中心结构，TS-Stellar 进一步分解层次技能，再配合小型回放缓存保持旧能力。论文在 LIBERO 和 AgiBot 真机任务中展示持续学习收益。局限是依赖每个新任务的机器人示范、已知任务阶段和训练更新，潜在簇难以解释或直接调用；专家容量固定、真机任务与训练步数有限，官方代码尚未公开。

- **WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2607.06988)
  - **摘要：** WAM-TTT 不把人类视频硬翻译成机器人动作，而是在冻结的世界—动作模型中设置轻量快速记忆，通过自监督视频预测在测试时吸收无标签人类视频；训练阶段再用成对人机数据和元训练，让这份视觉记忆能够影响机器人控制。这样同一示范可重复用于新任务变体。局限是仍需昂贵的人机配对元训练，测试时要更新记忆参数，效果取决于视频与机器人任务的相位对齐；代码和更广泛真机验证仍缺失。

## Failure-Driven Post-Training

这一部分收录“发现失败—重建环境—生成针对性经验—再训练”的闭环。它目前不一定属于机械臂技能学习，但为具身记忆如何由失败形成提供重要参照。

- **World Engine: Towards the Era of Post-Training for Autonomous Driving** — *arXiv 2026*  [Paper](https://arxiv.org/abs/2606.19836)  [Code](https://github.com/OpenDriveLab/WorldEngine)
  - **摘要：** World Engine 从真实驾驶日志中挖掘基础策略的失败场景，用 3D Gaussian Splatting 重建可交互环境，再由行为世界模型生成多样、反应式的危险变体，最后用带行为约束的强化学习定向后训练策略。其核心启示是把失败经验变成可反复练习的“情景记忆”。局限是工作面向自动驾驶而非机器人操作，高度依赖重建、交通行为模型、奖励和仿真真实性；迁移到接触丰富的示教学习仍属于研究设想。

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a paper.

## License

The repository license has not been selected yet. See [LICENSE](LICENSE).
