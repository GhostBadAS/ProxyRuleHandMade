ssh root@192.168.1.5
wget http://154.17.224.29/public/smbox-manage.sh?user=6094813866 -O manage.sh && chmod +x manage.sh && ./manage.sh
wget http://154.17.224.29/public/smbox-manage2.sh -O manage.sh && chmod +x manage.sh && ./manage.sh
cd /sbdir && rm -f cache.db && cd / && echo "已删除 /sbdir/cache.db 并返回根目录"