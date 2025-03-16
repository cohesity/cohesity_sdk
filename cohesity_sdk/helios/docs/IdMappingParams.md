# IdMappingParams

Specifies the params of the user id mapping info of an Active Directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sid_mapped_to_unix_root_user** | **str** | Specifies the sid of an Active Directory domain user mapping to unix root user. | 
**user_id_mapping_params** | [**UserIdMappingParams**](UserIdMappingParams.md) | Specifies the information about how the Unix and Windows users are mapped for this domain. | 

## Example

```python
from cohesity_sdk.helios.models.id_mapping_params import IdMappingParams

# TODO update the JSON string below
json = "{}"
# create an instance of IdMappingParams from a JSON string
id_mapping_params_instance = IdMappingParams.from_json(json)
# print the JSON string representation of the object
print(IdMappingParams.to_json())

# convert the object into a dict
id_mapping_params_dict = id_mapping_params_instance.to_dict()
# create an instance of IdMappingParams from a dict
id_mapping_params_from_dict = IdMappingParams.from_dict(id_mapping_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


