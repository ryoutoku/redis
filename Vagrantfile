# -*- mode: ruby -*-
# vi: set ft=ruby :

proxy = ""
porxy_port = ""

Vagrant.configure("2") do |config|

  # 使用するboxの設定
  # Ubuntu server 14.04
  config.vm.box = "ubuntu/trusty64"

  # ポート
  config.vm.network "forwarded_port", guest: 8065, host: 8065

  # ホストオンリーアダプタをipアドレス固定で追加
  config.vm.network "private_network", ip: "192.168.56.101"

  # virtualboxの実行設定
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "2048"
  end

  # redisの設定ファイルのコピー
  config.vm.provision "file", source: "./conf/redis.conf", destination: "/home/vagrant/redis.conf"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update

    # redisインストール
    sudo apt-get install redis-server -y

    # pip, redis.pyインストール
    apt-get install python-pip -y
    pip install redis

    # redis実行
    redis-server /home/vagrant/redis.conf &
  SHELL
end