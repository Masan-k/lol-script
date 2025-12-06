# lol-script

https://masan-k.github.io/lol-script/

## 概要 
ライアットゲームズが開発したパソコン向けゲーム「リーグ・オブ・レジェンド（League of Legends、以下LoL）」に関するデータを扱います。  
扱う主なデータは[ライオットゲームズの開発者向け公式サイト](https://developer.riotgames.com/docs/lol)を利用しています。  
また、LoLのスマホ版アプリ「ワイルドリフト」の情報も扱いますが「ワイルドリフト」はAPIやJSONファイルが存在しないため公式ホームページを使います。 
このリポジトリは、API・スクリプトの検証が目的のためUIの作り込みはしません。

## [CHAMPION LIST](www/champion.html)
各チャンピオンの名称とロールを確認します。

## ツール
- [全チャンピオンの画像を公式サイトから一括ダウンロードするスクリプト@python](https://github.com/Masan-k/lol-script/tree/fafe13d237428fdf00f5a1f43df51876e31e121d/tool/getChampionImage)  
  imput  : champion.json  
  output : champion.id.png
