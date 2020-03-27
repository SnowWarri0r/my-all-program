import requests
import json
def print_hitokoto(): 
    a=1;koto=[];text=''
    for x in range(30):
        url=requests.get("https://v1.hitokoto.cn");
        html=url.text.encode("utf-8");
        text = str(a)+"."+json.loads(html)['hitokoto']+"  from:"+json.loads(html)['from'];
        koto.append(text);
        fileWrite(koto);      
        a=a+1;     
def fileWrite(data):
    f=open('D:\\hitokoto.txt','w'); 
    for b in range(len(data)):
        f.write(str(data[b])+"\n");
    f.close();         
def main():
   print_hitokoto();
if __name__=='__main__':
    main()
        
        

                
    

        

        

