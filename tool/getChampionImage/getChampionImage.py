import os,json,requests
json_open = open('input/champion.json','r');
json_load = json.load(json_open);
save_dir_square = 'output/square'
save_dir_splash = 'output/splash'
base_url_square = 'https://ddragon.leagueoflegends.com/cdn/15.24.1/img/champion/'
base_url_splash = 'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/'

os.makedirs(save_dir_square, exist_ok=True)
os.makedirs(save_dir_splash, exist_ok=True)

for v in json_load['data'].values():
  #file_name = v['id'] + '_0.jpg'
  #save_path_splash = os.path.join(save_dir_splash,file_name)
  #download_url_splash = base_url_splash + file_name 
  #res = requests.get(download_url_splash).content

  file_name = v['id'] + '.png'
  save_path_square = os.path.join(save_dir_square,file_name)
  download_url_square = base_url_square + file_name 
  res = requests.get(download_url_square).content
 
  with open(save_path_square, mode='wb') as f:
    f.write(res) 

