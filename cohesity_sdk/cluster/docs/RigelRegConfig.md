# RigelRegConfig

Specifies the Rigel Registration Config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_plane_connection_info** | [**RigelConnectionInfo**](RigelConnectionInfo.md) |  | [optional] 
**data_plane_connection_info** | [**RigelConnectionInfo**](RigelConnectionInfo.md) |  | [optional] 
**is_certificate_valid** | **bool** | Flag to indicate if certificate is valid. | [optional] 
**reg_info** | [**RigelClaimInfo**](RigelClaimInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.rigel_reg_config import RigelRegConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RigelRegConfig from a JSON string
rigel_reg_config_instance = RigelRegConfig.from_json(json)
# print the JSON string representation of the object
print(RigelRegConfig.to_json())

# convert the object into a dict
rigel_reg_config_dict = rigel_reg_config_instance.to_dict()
# create an instance of RigelRegConfig from a dict
rigel_reg_config_from_dict = RigelRegConfig.from_dict(rigel_reg_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


