# ObjectSiteParam

Specifies Site recovery parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_library_params** | [**List[OneDriveParam]**](OneDriveParam.md) | Specifies the parameters to recover a document library | [optional] 
**owner_info** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) |  | 

## Example

```python
from cohesity_sdk.models.object_site_param import ObjectSiteParam

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectSiteParam from a JSON string
object_site_param_instance = ObjectSiteParam.from_json(json)
# print the JSON string representation of the object
print(ObjectSiteParam.to_json())

# convert the object into a dict
object_site_param_dict = object_site_param_instance.to_dict()
# create an instance of ObjectSiteParam from a dict
object_site_param_from_dict = ObjectSiteParam.from_dict(object_site_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


