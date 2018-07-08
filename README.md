Vagrant + Docker(mattermost)
====

## 概要

Vagrantを使ってVirtualBox(Ubuntu14.04)内にredisを起動する
ホスト側redisを使用してpub/subを試すサンプル

subscriber.py側で
* redisにデータを追加
* redisのsubを実行

publisher.py側で
* redisのデータ変更を監視
* 変更があった場合、pubを実行

## Requirement
- VirtualBox
- Vagrant
- Python3

## Usage
1. 以下コマンドを実行し、VMを起動
    > vagrant up
2. 以下コマンドを実行し、publisher側を起動
    > python src/publisher.py
3. 以下コマンドを実行し、subscriber側を起動
    > python src/subscriber.py
4. 起動した後、subscriber側でキーボード入力