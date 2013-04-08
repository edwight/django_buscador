<VirtualHost *:90>

    WSGIScriptAlias / /home/sergio/code/recetario_mdw/recetario/recetario/wsgi.py

    Alias /static/ /home/sergio/code/recetario_mdw/recetario/recetario/static/
    Alias /media/ /home/sergio/code/recetario_mdw/recetario/recetario/carga/

    <Directory /home/sergio/code/recetario_mdw/recetario>
    <Files wsgi.py>
    Order deny,allow
    Allow from all
    </Files>
    </Directory>

    <Directory /home/sergio/code/recetario_mdw/recetario/recetario/static/>
    Order deny,allow
    Allow from all
    </Directory>

    <Directory /home/sergio/code/recetario_mdw/recetario/recetario/carga/>
    Order deny,allow
    Allow from all
    </Directory>

	ErrorLog ${APACHE_LOG_DIR}/error.log

	# Possible values include: debug, info, notice, warn, error, crit,
	# alert, emerg.
	LogLevel warn

	CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
