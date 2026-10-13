# Webviewer

Webviewer is (or will be) a web-based viewer with is part of Quickiebase.

Endpoints will include

* `/` = lists information about this Quickiebase installation
* `/db` = lists databases
* `/db/{dbname}` = lists the collections for database {dbname}
* `/db/{dbname}/col/{colname}` = lists information about collection {colname}, including showing its contents
* `/db/{dbname}/col/{colname}/id/{id}` = lists information about one record in a collection with the key {id}

At a later stage it will be possible to edit the contents of a collection or record, and create/delete databases, collections, and records. 

## Information about collections

We might later on add information in collections amounting to something like a dastabase schema.

## Default fields

A record in Quickieview is entirely free-form , so it can have whatever fields it likes. But it might be nice to have defaults.

For a collection we might have default fields, for each one we would have:

* field name
* field index -- this affects how it is displayed in webviewer
* expected field type, e.g. int, float, bool, None, list, array, foreign key
* default value -- if the field is not present it takes this value

We could have a foreign key to another field as a field type. Then, in webviewet when we click on the value it goes to the
collection/record which is being pointed to.

### How field types might work

```
FieldType = SimpleType | CompositeType

SimpleType = int | float | bool | None | FK {collectionName}

CompositeType = List {FieldType}01
              | Array {FieldType}01
```




