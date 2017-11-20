# vol. 1.0

# 1-生成所有的组合到数据库
# 2-判断所有的组合分值
# 3-计算拿到13张牌，各类组合几率是

poke='1384'
poke=sorted(poke)
print(poke)
poke=poke+['1']
poke=sorted(poke)
print(poke)
card=poke[0]+poke[1]+poke[2]+poke[3]+poke[4]
print(card)

# j=jjhaxbe
print(poke+card)
