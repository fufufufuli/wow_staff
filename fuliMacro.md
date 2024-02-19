## 键位
|q|e|r|t|`|y|h|ctr+q|alt+q|qlt+e|alt+r|caps|
|-|-|-|-|-|-|-|-|-|-|-|-|
|1|2|3|4|5|6|z|x|c|v|f|g|
|shift+f|shift+g|alt+c|b|ctr+1|ctr+2|ctr+3|ctr+4|alt+x||||
|F1|F2|F3|alt+1|alt+2|alt+3|alt+v|ctr+w|ctr+e|ctr+r|``|``|
|shift+1|shift+2|shift+3|shift+q|shift+w|shift+e|shift+r|shift+t|shift+z|shift+x|shift+v|alt+f|
## 通用宏
#### 屏幕中间技能
```
/click ExtraActionButton1
```
```
/castrandom [flyable] 暴怒角斗士的冰霜巨龙, 罪孽角斗士的噬魂者
/castrandom [noflyable] 迅捷幽灵虎, 白色邪恶作战刃豹
```
#### 标记队友 1星星，2大饼，3紫菱，4三角，5月亮，6方块，7红x，8骷髅
```
/script SetRaidTarget("player",8)
/script SetRaidTarget("party1",2)
/script SetRaidTarget("party2",6)
/script SetRaidTarget("party3",)
/script SetRaidTarget("party4",)
```
```
/focus [@mouseover,exists][@target]
```
```
/use 10
```
```
/use 13
```
```
/use 14
```
```
/petmoveto
```
#### 焦点打断
```
/cancelaura 寒冰屏障
/cast [@focus]责难
/cast [@focus]法术反制
```
```
/cast [@arena1] 深度冻结
/cast [@arena1] 制裁之锤
```
```
/cast [@arena1] 变形术
/cast [@arana1] 忏悔
```
```
/cast [@arena1] 法术反制
```
```
/cast [@arena1] 火焰冲击
```
```
/cast [@party1] 清洁术
/cast [@party1] 驱散魔法
```
```
/cast [@player] 驱散魔法
/cast [@player] 清洁术
```
## warrior
```
#showtooltip [stance:1/3]拳击;[stance:2]盾击
/cast [@focus,stance:1/2,noequipped::盾牌] 狂暴姿态;[@focus,stance:1/2,equipped:盾牌] 盾击;[@focus,stance:3] 拳击
```
## druid
```
#showtooltips [nocombat,nostealth] 潜行;野性冲锋
/cast [nocombat]!潜行; [nostance:2]猎豹形态(变形)
```
## priest
```
/cast [@mouseover,harm,nodead][harm,nodead]精神控制;[help][]治疗术
```
```
/cast [harm,nodead]法力燃烧;[@mouseover,help,nodead][help,nodead][]信仰飞跃
```
```
/cast [harm,nodead]心灵尖刺;[help][]快速治疗
```
```
/cast [harm,nodead]惩击;[help][]快速治疗
```
```
/cast [@mouseover,harm,nodead][harm,nodead][@targettarget,harm,nodead][]暗言术：灭
```
#### 进攻驱散
```
/cast [@mouseover,harm,nodead][harm,nodead][@targettarget,harm,nodead][]驱散魔法
```
```
/cast [@mouseover,harm,nodead][harm,nodead][]苦修
```
```
/castsequence 心灵之火,心灵意志
```
```
/cast [@mouseover,harm,nodead][@targettarget,harm,nodead][harm,nodead][]暗影恶魔
/petattack
```
```
/castsequence reset=20 真言术：韧,暗影防护
```
```
/castsequence 神圣之火,心灵震爆
```
```
/cast [@mouseover,harm,nodead][harm,nodead][@targettarget,harm,nodead][]心灵震爆
```
```
/cast [@mouseover,harm,nodead][harm,nodead]束缚亡灵;[help][]联结治疗
```
```
/cast [@mouseover,help,nodead][help]真言术：盾
/castsequence  reset=10 暗言术：痛,噬灵疫病
```
#### aoe&抓潜行
```
/cast [@mouseover,harm,nodead][harm,nodead][]精神灼烧
```
#### 焦点灭
```
/cast [@focus,harm,nodead] [harm,nodead][]暗言术：灭
```
```
/cast [@player] 防护恐惧结界
```
```
/cast [@player] 能量灌注
```
## mage
```
/cast [nopet][@pet,dead]召唤水元素;冰冻术
/petattack
```
```
/dismount
/cancelaura 寒冰屏障
/cast [@mouseover,harm,nodead][harm,nodead][]冰枪术
```
```
/dismount
/cancelaura 寒冰屏障
/cast [@mouseover,harm,nodead][harm,nodead][]寒冰箭
```
```
/cancelaura 寒冰屏障
/cast [@mouseover,harm,nodead][harm,nodead][]深度冻结
```
```
/cancelaura 寒冰屏障
/cast [@mouseover,harm,nodead][harm,nodead][]火焰冲击
```
```
/cancelaura 寒冰屏障
/stopcasting
/cast [@mouseover,harm,nodead][harm,nodead][]法术反制
```
```
/cast [@mouseover,help,nodead][help,nodead][]解除诅咒
```
```
/cast [@mouseover,harm,nodead][harm,nodead][]霜火之箭
/petattack
```
```
/cast 冰冷血脉
/use 14
```
```
/dismount
/cancelaura 寒冰屏障
/cast [@mouseover,harm,nodead][harm,nodead][]变形术
/petfollow
```
```
/castsequence 法师护甲,霜甲术
```
```
/cast [@focus,combat]火焰冲击;迅捷褐色马
```
```
#showtooltip 烈焰宝珠
/use 10 
/use 14
/cast 烈焰宝珠
```
```
#showtooltip 
/cast [@cursor]暴风雪
```
## paladin
```
#showtooltip 审判
/cast [@mouseover,harm,nodead][harm,nodead]审判;圣光道标
```
```
/cast [@mouseover,harm,nodead][harm,nodead]十字军打击;圣光闪现
```
```
/cast [@mouseover,harm,nodead][harm,nodead][]责难
/cast 十字军打击
```
##### 队友牺牲
```
/cast [@party1]牺牲之手
```
##### 队友保护
```
/cast [@party1]保护之手
```
##### 队友自由
```
/cast [@party1]自由之手
```
##### 自己自由
```
/cast [@player]自由之手
```
##### 自己保护
```
/cast [@player]保护之手
```
```
/cast [harm,nodead]愤怒之锤;[help][]圣光术
```
```
#showtooltip 
/cast [@mouseover,harm,nodead][harm,nodead]清算之手;正义防御
```
```
/cast [@mouseover,harm,nodead][harm,nodead][]超度邪恶
```




