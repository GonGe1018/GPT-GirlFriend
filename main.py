#"chatData_org.json"을 "chatData.json"로 이름을 바꿔주세요.
#"key.txt"를 만들어 api key를 넣어주세요.
import openai
import json

openai.api_key = open("key.txt","r").readline()

messages=[]

chatData=open(file='./chatData.json',mode='r',encoding="UTF-8").read()#json파일 가져와서 딕셔너리로 변환
chatDict = json.loads(chatData)

for i in range(0,len(chatDict)):#messages리스트에 기존대화 목록 추가
    messages.append(chatDict[str(i)])

while True:
    msgInput=input("나 : ")

    if(msgInput=="0"): break
    else: messages.append({"role": "user", "content": msgInput})

    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": response})
    except:
        response="오류"

    print("여자친구 :",response)
    

msgDict={}
for i in range(0,len(messages)):
    msgDict[str(i)]=messages[i]   
print(msgDict)
_json = json.dumps(msgDict, indent = 4, sort_keys = True, ensure_ascii = False)#딕셔너리에서 json으로 변환
newFile = open('./chatData.json', 'w',encoding="UTF-8")#저장
newFile.write(_json)
newFile.close