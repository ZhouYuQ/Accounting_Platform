
# import yaml
#
# with open("./data.yml", "r",encoding="utf-8") as f:
#     r = yaml.safe_load_all(f)
#     for i in r:
#         print(i)

from utils.YamlUtil import YamlReader

res = YamlReader("./data.yml").data_all()
# print(res)

# res = YamlReader("./data.yml").data_all()

print(res)