# AmselDrosselMaise

Bandbreitenlimitierung für den Mirror auf dem schlimmen _PHP_ Webhost.

Immer schön mit der Holzhammermethode gelöst, sprich das Script ließt die angefragten Dateien in n Kilobyte Chunks ein, und schläft dazwischen immer ein bisschen. :zzz:

Habe dies für einen _torrent Webseed_ am laufen, somit ist der _torrent_ immer verfügbar, und der Traffic hält sich in Grenzen. :cow: :pig:

Vor dem Hochladen die __htaccess__ in `.htaccess` umbenennen.

Es empfiehlt sich auch die __dl.php__ in `.dl.php` umzubenennen, damit diese nicht im Filelisting rumfliegt.

Dazu muss man in der `.htaccess` die entsprechende Regel natürlich ändern:

	RewriteRule . .dl.php

Viel Spaß!

:octocat:
