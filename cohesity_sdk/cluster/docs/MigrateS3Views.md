# MigrateS3Views

Specifies the parameters required to perform the S3 Migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_migration_action** | **str** | Specifies the target S3 migration state for the Views specified in the viewIds parameter. Supported Migration States are: [Enable, Cancel, Pause, Resume]. | 
**view_ids** | **List[int]** | Specifies the list Views IDs on which the migration action will be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.migrate_s3_views import MigrateS3Views

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateS3Views from a JSON string
migrate_s3_views_instance = MigrateS3Views.from_json(json)
# print the JSON string representation of the object
print(MigrateS3Views.to_json())

# convert the object into a dict
migrate_s3_views_dict = migrate_s3_views_instance.to_dict()
# create an instance of MigrateS3Views from a dict
migrate_s3_views_from_dict = MigrateS3Views.from_dict(migrate_s3_views_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


