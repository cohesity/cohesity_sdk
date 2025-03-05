# ObjectTypeWindowsClusterParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_source_type** | **str** | Specifies the type of cluster resource this source represents. | [optional] 

## Example

```python
from cohesity_sdk.models.object_type_windows_cluster_params import ObjectTypeWindowsClusterParams

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectTypeWindowsClusterParams from a JSON string
object_type_windows_cluster_params_instance = ObjectTypeWindowsClusterParams.from_json(json)
# print the JSON string representation of the object
print(ObjectTypeWindowsClusterParams.to_json())

# convert the object into a dict
object_type_windows_cluster_params_dict = object_type_windows_cluster_params_instance.to_dict()
# create an instance of ObjectTypeWindowsClusterParams from a dict
object_type_windows_cluster_params_from_dict = ObjectTypeWindowsClusterParams.from_dict(object_type_windows_cluster_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


