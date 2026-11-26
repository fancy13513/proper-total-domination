# 查新与研究价值评估

**结论（2026-11-26）。** 建议把这个结果写成计算图论研究短文，先送给熟悉图支配或组合计算的研究者审读。奇数环面的完整分类回答了已发表论文的一个明确问题。宽五情况下的最少标记数给出第二个无限族定理，可独立核算。国内数学、信息与计算科学或计算机理论方向的本科毕业论文，以此为核心，研究内容和可用工作量已够。学校对作者个人完成情况、写作与答辩的考核另行进行。

## 一、最接近的文献

| 文献及核对范围 | 与本稿的关系 |
|---|---|
| Chatterjee、Jent、Osborn、Zhang，2024，期刊 PDF。[Proper total domination in graphs](https://doi.org/10.47443/ejm.2024.024) | 确立本稿使用的参数，讨论道路、圈、普通网格及其他图类。普通网格的边界不同。 |
| Osborn、Zhang，2026，第 3 节末、第 4 节及已有分类。[From princes on chessboards to proper total domination in graphs](https://doi.org/10.61091/jcmcc129-03) | 两条奇边均至少为 5 的环面存在性被明确列为问题。文中另一个有编号的 Problem 2.8 是圆柱问题，不能混称。 |
| Osborn、Zhang，2026，相关工作段落。[Proper Total Domination in Generalized Fans and Wheels](https://doi.org/10.3390/sym18071092) | 同一作者再次将两条奇边至少为 5 的环面分类写为未知，并说明环面等图的一般精确支配数尚不清楚。后一句本身不能证明某个特定宽度此前未被单独求出。 |
| Bouznif、Darlay、Moncel、Preissmann，2019，摘要、图族定义与周期方法。[Exact values for three domination-like problems](https://doi.org/10.23638/DMTCS-21-3-12) | 重要的方法先例。研究三个有关辨识或定位的最优化目标，其中也考虑环面。不能把转移图、最短闭游走或 min-plus 周期检验证明写成本文发明的方法。 |
| Wehrmann、Koster，2026，摘要。[Efficient total domination and related invariants in torus graphs](https://doi.org/10.1016/j.dam.2026.03.047) | 同样研究两个圈的笛卡尔积，但要求每一顶点的标记邻居数都等于同一常数 k。本稿要求相邻顶点的计数不同。 |
| Czerwiński、Grytczuk、Żelazny，2009；Chartrand 等，2009。[Lucky labelings](https://doi.org/10.1016/j.ipl.2009.05.011) · [Multiset chromatic number](https://doi.org/10.21136/MB.2009.140654) | 在四正则图上以两种标签区分邻域和或颜色重数，与本题分辨相邻顶点的条件接近，但还须落实全支配的正性和最小基数。查到的这些文献未给出本文的两条结论。 |
| Osborn，2026 年 6 月博士论文，已核对大学存档、摘要及研究主题。[From Total Domination to Graph Coloring](https://scholarworks.wmich.edu/dissertations/4275/) | 是最值得继续逐页核对的来源之一。公开全文下载接口返回 HTTP 403；另检索作者、题名、关键词及其他公开入口，未取得全文。学位论文可能含有未收录在期刊摘要中的局部结果。 |

## 二、检索记录和边界

核对过的公开渠道包括期刊官网及可取得的论文全文、arXiv 论文全文检索、大学学位论文存档、开放网页索引。还分别尝试限定 arXiv、Zenodo、GitHub、Hexagon 及中文学术站点域名的网页检索。部分数据库只有公开索引可见；未完成 MathSciNet、zbMATH、知网和万方的逐库引文检索。没有将默认返回的相似主题算作全文核查。

可重复检索的代表性英文检索式如下。每组应分别用 toroidal grid、cyclical graph、torus graph、Cartesian product of cycles 替换图族名称。

1. `"proper total domination" "cyclical graphs" odd Osborn Zhang`
2. `"proper total domination number" toroidal C5 Cartesian product cycles`
3. `"proper total dominating set" "width five" torus`
4. `"lucky labeling" OR "multiset chromatic number" Cartesian product cycles`
5. `min-plus transfer matrix domination circular strips toroidal grids`
6. `"From Total Domination to Graph Coloring" Osborn cyclical graphs`

中文检索词包括“环面网格图”“适当全支配”“邻和可区别”“笛卡尔乘积”。例如，[广州大学学报相关论文](https://xb.gzhu.edu.cn/zkb/CN/Y2022/V21/I1/34)的权重还涉及顶点和关联边，不对应本稿的开邻域计数。

本次未检出这两个精确定理的先例。对存在性分类的历史依据较直接：有原题和作者后续重述。对宽五公式，只能给出检索未命中的判断。文献查新不可能排除私人手稿、在审论文或未建索引的资料。正式投稿前，值得让独立读者对博士论文的笛卡尔积章节和原论文的前向引用补查一次。

## 三、证明的质量和局限

| 项目 | 已落实 | 对论文的含义 |
|---|---|---|
| 定义对齐 | 与期刊论文同用开邻域、全支配、相邻计数不等；程序覆盖两处环面接缝 | 读者能用原文逐项核对 |
| 无限尺寸 | 局部窗口引理及显式种子贡献存在性；宽五用完整距离矩阵恒等式归纳 | 两个结论都有从有限计算推出无限范围的证明 |
| 数值可信度 | 原始构造、直接穷举、转移图以及改变编码和计费方式的第二实现交叉复核 | 能发现漏接缝、列重复计费、只看对角线等常见错误 |
| 理论深度 | 除完整分类及宽五最优值外，给出一般奇数环面的组合计数下界 | 有可手验的理论内容，创新集中于这一图族 |
| 待补证据 | 尚未获得独立研究者的数学审读；尚未逐页查到上述学位论文 | 目前应称为可复现的研究草稿；实际录用和首发性未定 |

## 四、和本科毕业论文要求对照

浙江师范大学的公开评分材料把理论基础、文献综述、研究方案、分析论证、实验数据、创新以及答辩分别评价。华东师范大学的计算机本科评分材料也关注方法、数据和理论或实际问题分析的深度。此处引用作参照，具体培养方案和学校仍以实际要求为准。[浙江师范大学评分材料](https://sxxy.zjnu.edu.cn/_upload/article/files/65/6b/78af25c14822b76b46a3579ee078/a0c67958-68de-4289-b129-546b5f701617.pdf) · [华东师范大学计算机本科评分标准](https://cs.ecnu.edu.cn/_upload/article/files/58/c6/0230efc349e6936dcfa1578ffdcf/23ed5b12-0c2f-4346-a091-606e81e6b09b.pdf)

**判断。** 选题明确、完整数学结果、算法分析和可复现实验四项已有充分内容。这个判断针对课题质量与研究深度，未给学生个人打分。现有材料是仓库研究稿，实际毕业论文仍要按本校要求写作，并能在答辩中自行说明三个关键问题：局部窗口为什么覆盖所有尺寸、闭游走为什么对应环面、最低费用数列暂时出现周期为何不足以推断无限周期。项目内已记录 AI 参与事实。本仓库及稿件未对外投稿，亦未向原作者发送消息。
