import os,json,requests
json_open = open('input/champion.json','r');
json_load = json.load(json_open);
base_url = 'https://ddragon.leagueoflegends.com/cdn/15.24.1/img/champion/'
save_dir = 'output'

for v in json_load['data'].values():
  file_name = v['id'] + '.png'
  
  save_path = os.path.join(save_dir,file_name)
  download_url = base_url + file_name 
  res = requests.get(download_url).content
 
  with open(save_path, mode='wb') as f:
    f.write(res)
