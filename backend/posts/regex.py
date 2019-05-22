import re
def parse_text(text):
    field =  re.compile("<Comment: (\d+)isp(\w+)who([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2][:-19],i[2][-19:]))
        
    return true_result

def parse_checklist(text):
    field = re.compile("<Checklist: (\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)where(\d+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2][:-1],i[2][-1:]))
        
    return true_result

#[<Title: 10spcreate 테스트nacreate 테스트>]
def parse_title(text):
    field = re.compile("<Title: (\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2]))
        
    return true_result