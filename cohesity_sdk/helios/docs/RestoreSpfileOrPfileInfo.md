# RestoreSpfileOrPfileInfo

Specifies information related to restoring Spfile/Pfile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_location** | **str** | Specifies the location where spfile/file will be restored. If this is empty and shouldRestoreSpfileOrPfile is true we restore at default location: $ORACLE_HOME/dbs | [optional] 
**should_restore_spfile_or_pfile** | **bool** | Specifies whether to restore spfile/pfile or skip it. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.restore_spfile_or_pfile_info import RestoreSpfileOrPfileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreSpfileOrPfileInfo from a JSON string
restore_spfile_or_pfile_info_instance = RestoreSpfileOrPfileInfo.from_json(json)
# print the JSON string representation of the object
print(RestoreSpfileOrPfileInfo.to_json())

# convert the object into a dict
restore_spfile_or_pfile_info_dict = restore_spfile_or_pfile_info_instance.to_dict()
# create an instance of RestoreSpfileOrPfileInfo from a dict
restore_spfile_or_pfile_info_from_dict = RestoreSpfileOrPfileInfo.from_dict(restore_spfile_or_pfile_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


