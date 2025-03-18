# FilerLifecycleManagement

Specifies the filer Lifecycle policy of a NFS/SMB view. If not specified no Lifecycle management is performed for entites in filer view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[FilerLifecycleRule]**](FilerLifecycleRule.md) | Specifies Lifecycle configuration rules for a filer view. A maximum of 100 rules can be specified. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.filer_lifecycle_management import FilerLifecycleManagement

# TODO update the JSON string below
json = "{}"
# create an instance of FilerLifecycleManagement from a JSON string
filer_lifecycle_management_instance = FilerLifecycleManagement.from_json(json)
# print the JSON string representation of the object
print(FilerLifecycleManagement.to_json())

# convert the object into a dict
filer_lifecycle_management_dict = filer_lifecycle_management_instance.to_dict()
# create an instance of FilerLifecycleManagement from a dict
filer_lifecycle_management_from_dict = FilerLifecycleManagement.from_dict(filer_lifecycle_management_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


