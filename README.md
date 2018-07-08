Vagrant + Docker(mattermost)
====

## 概要

Vagrantを使ってVirtualBox(Ubuntu14.04)内にチャットサーバ(mattermost)を起動する

## Requirement

- VirtualBox
- Vagrant
- vagrant-proxyconf  
https://github.com/tmatilai/vagrant-proxyconf

## Usage

1. `Vagrantfile`の以下部分に、proxyサーバのIPアドレスとproxyサーバのポートを設定する
    ```
    proxy = ""
    porxy_port = ""
    ```
1. 以下コマンドを実行し、VMを起動
    > vagrant up

1. VMが起動した後、以下にアクセスする
    > http://{ホストOSのIPアドレス}:8065/
