import wikipedia
import requests,os,zipfile
words = requests.get("https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt").text.splitlines()
print(len(words))
m = []
for i in words:
    m = m + wikipedia.search(i,results=500)
    print(len(m))
for i in m:
    print(i)
    try:
        with open("Openswiki/"+i+".txt","w") as f:
            f.write(wikipedia.summary(i,sentences=30))
    except:
        print("FAILED TO EXTRACT",i)
        os.remove("Openswiki/"+i+".txt")

zip = zipfile.ZipFile("Openswiki.zip", "w", zipfile.ZIP_DEFLATED)
for m in os.listdir("Openswiki/"):
    zip.write("Openswiki/"+m)
zip.close()
