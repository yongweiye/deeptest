# coding=utf-8


import  configparser

config=configparser.ConfigParser()

section=config.add_section("sfa")

config.set("sfa","YY","DeepTest")
config.set("sfa","WW","DogNum")

config.add_section("platform")

with open("config.ini","w") as configFile:
    config.write(configFile)

# config.read("config.ini")

sections=config.sections()
print sections

for sec in sections:
    options=config.options(sec)
    print options

    for option in options:
        print config.get(sec,option)
