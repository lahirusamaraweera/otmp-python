service nginx stop && \
    rm /etc/nginx/sites-available/default  && \
    ln -s /code/docker/nginx/nginx_config /etc/nginx/sites-available/default

service nginx start