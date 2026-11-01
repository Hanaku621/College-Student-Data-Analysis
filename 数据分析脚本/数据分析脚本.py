import pandas as pd
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')

if not os.path.exists('分析结果图'):
    os.makedirs('分析结果图')

print("开始读取数据并生成图表...")

df_platform = pd.read_csv('03_年轻人娱乐平台使用率与时长变化.csv', encoding='utf-8-sig')

df_platform['时长净增(%)'] = df_platform['时长净增(%)'].astype(str).str.replace('+', '', regex=False)
df_platform['时长净增(%)'] = pd.to_numeric(df_platform['时长净增(%)'])

fig, ax1 = plt.subplots(figsize=(8, 5))
bars = ax1.bar(df_platform['平台类型'], df_platform['使用率(%)'], color='skyblue', label='使用率(%)', width=0.5)
ax1.set_ylabel('使用率 (%)', fontsize=12)
ax1.set_title('年轻人各类型平台使用率与时长变化', fontsize=15)
ax1.set_ylim(0, 115)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f'{yval}%', ha='center', va='bottom')

ax2 = ax1.twinx()
ax2.plot(df_platform['平台类型'], df_platform['时长净增(%)'], color='red', marker='o', linewidth=2, label='时长净增(%)')
ax2.set_ylabel('时长净增 (%)', fontsize=12)
ax2.axhline(0, color='gray', linestyle='--')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right')

plt.tight_layout()
plt.savefig('分析结果图/图1_平台使用与时长变化.png', dpi=150)
plt.close()


df_offline = pd.read_csv('05_年轻人线下娱乐选择率.csv', encoding='utf-8-sig')
df_offline = df_offline.sort_values(by='选择率(%)', ascending=True)

plt.figure(figsize=(8, 5))
plt.barh(df_offline['线下娱乐类型'], df_offline['选择率(%)'], color='mediumseagreen')
plt.xlabel('选择率 (%)', fontsize=12)
plt.title('年轻人线下娱乐类型选择率', fontsize=15)

for i, v in enumerate(df_offline['选择率(%)']):
    plt.text(v + 0.5, i, f'{v}%', va='center')

plt.tight_layout()
plt.savefig('分析结果图/图2_线下娱乐选择率.png', dpi=150)
plt.close()


df_attitude = pd.read_csv('04_年轻人娱乐时间与态度.csv', encoding='utf-8-sig')

plt.figure(figsize=(10, 5))
bars = plt.bar(df_attitude['指标'], df_attitude['数值(%)'], color='coral', width=0.5)
plt.ylabel('比例 (%)', fontsize=12)
plt.title('年轻人娱乐时间与态度指标', fontsize=15)
plt.xticks(rotation=30, ha='right')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval}%', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('分析结果图/图3_娱乐时间与态度.png', dpi=150)
plt.close()


df_ai = pd.read_csv('01_AI平台活跃渗透率.csv', encoding='utf-8-sig')
df_ai = df_ai.sort_values(by='活跃渗透率(%)', ascending=True)

plt.figure(figsize=(8, 4))
plt.barh(df_ai['平台'], df_ai['活跃渗透率(%)'], color='slateblue', height=0.6)
plt.xlabel('活跃渗透率 (%)', fontsize=12)
plt.title('国内主流AI原生App活跃渗透率 (2026.08)', fontsize=15)

for i, v in enumerate(df_ai['活跃渗透率(%)']):
    plt.text(v + 0.5, i, f'{v}%', va='center')

plt.tight_layout()
plt.savefig('分析结果图/图4_AI平台渗透率.png', dpi=150)
plt.close()


df_demo = pd.read_csv('02_AI用户年龄与城市分布.csv', encoding='utf-8-sig')
age_data = df_demo[df_demo['维度'] == '年龄']
city_data = df_demo[df_demo['维度'] == '城市']

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(age_data['占比(%)'], labels=age_data['类别'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
axes[0].set_title('AI用户年龄分布', fontsize=14)

axes[1].bar(city_data['类别'], city_data['占比(%)'], color='goldenrod', width=0.5)
axes[1].set_title('AI用户城市层级分布', fontsize=14)
axes[1].set_ylabel('占比 (%)')
for i, v in enumerate(city_data['占比(%)']):
    axes[1].text(i, v + 0.5, f'{v}%', ha='center')

plt.tight_layout()
plt.savefig('分析结果图/图5_AI用户画像.png', dpi=150)
plt.close()

print("✅ 全部完成！请打开当前文件夹下的【分析结果图】文件夹查看结果。")