import os, subprocess, json

repo_path="/custom-repo/ubuntu-18.04/images/"
repo_fqdn="customreg.epi.local:5010"

files = [ f for f in os.listdir(repo_path) if os.path.isfile(os.path.join(repo_path, f))]

for file in files:
    filename = file.replace('.tar','')
    print(f'---Filename: ' + filename)
    os.system(f"tar -xf "+os.path.join(repo_path, file)+" manifest.json")
    with open("manifest.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    imgtag= jsonObject[0]['RepoTags'][0]
    print(f'---JSONRepoTags: ' + imgtag)
    tag = imgtag[imgtag.rindex(':')+1:]
    img = imgtag[:imgtag.rindex(':')]
    os.system(f"""sudo docker image load --input """+os.path.join(repo_path, file))
    print(f'--- Img: '+ img)
    print(f'--- Tag: '+ tag)
    os.system(f"sudo docker image tag "+img+":"+tag+" "+repo_fqdn+"/"+img+":"+tag)
    os.system(f"sudo docker push "+repo_fqdn+"/"+img+":"+tag)
    # input("---------------------Press Enter to continue...")
