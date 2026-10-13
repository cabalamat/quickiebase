# Webviewer

Webviewer is (or will be) a web-based viewer with is part of Quickiebase.

Endpoints will include

* `/` = lists information about this Quickiebase installation
* `/db` = lists databases
* `/db/{dbname}` = lists the collections for database {dbname}
* `/db/{dbname}/col/{colname}` = lists information about collection {colname}, including showing its contents
* `/db/{dbname}/col/{colname}/id/{id}` = lists information about one record in a collection with the key {id}

At a later stage it will be possible to edit the contents of a collection or record, and create/delete databases, collections, and records. 