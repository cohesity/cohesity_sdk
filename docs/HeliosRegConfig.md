# HeliosRegConfig

Specifies the Helios Registration Config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Specifies the type of entity that is registered on Helios. | [optional] 
**rigel_reg_config** | [**RigelRegConfig**](RigelRegConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.helios_reg_config import HeliosRegConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosRegConfig from a JSON string
helios_reg_config_instance = HeliosRegConfig.from_json(json)
# print the JSON string representation of the object
print(HeliosRegConfig.to_json())

# convert the object into a dict
helios_reg_config_dict = helios_reg_config_instance.to_dict()
# create an instance of HeliosRegConfig from a dict
helios_reg_config_from_dict = HeliosRegConfig.from_dict(helios_reg_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


