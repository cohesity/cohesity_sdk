# AdFixedTypeParams

Specifies the properties accociated to a Fixed type user id mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **int** | Specifies the fixed Unix GID, when mapping type is set to kFixed. | 
**uid** | **int** | Specifies the fixed Unix UID, when mapping type is set to kFixed. | 

## Example

```python
from cohesity_sdk.helios.models.ad_fixed_type_params import AdFixedTypeParams

# TODO update the JSON string below
json = "{}"
# create an instance of AdFixedTypeParams from a JSON string
ad_fixed_type_params_instance = AdFixedTypeParams.from_json(json)
# print the JSON string representation of the object
print(AdFixedTypeParams.to_json())

# convert the object into a dict
ad_fixed_type_params_dict = ad_fixed_type_params_instance.to_dict()
# create an instance of AdFixedTypeParams from a dict
ad_fixed_type_params_from_dict = AdFixedTypeParams.from_dict(ad_fixed_type_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


