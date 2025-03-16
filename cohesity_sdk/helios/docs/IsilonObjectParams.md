# IsilonObjectParams

Specifies the common parameters for Isilon objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_nas_mount_protocols** | **List[str]** | Specifies a list of NAS mount protocols supported by this object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.isilon_object_params import IsilonObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of IsilonObjectParams from a JSON string
isilon_object_params_instance = IsilonObjectParams.from_json(json)
# print the JSON string representation of the object
print(IsilonObjectParams.to_json())

# convert the object into a dict
isilon_object_params_dict = isilon_object_params_instance.to_dict()
# create an instance of IsilonObjectParams from a dict
isilon_object_params_from_dict = IsilonObjectParams.from_dict(isilon_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


