# PrivateNetworkInfo

Specifies the object parameters to create Azure Snapshot Manager Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Specifies the subnet for creating a private endpoint. | [optional] 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the region of the virtual network. | [optional] 
**subnet** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the subnet for creating a private endpoint. | [optional] 
**vpn** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the virtual network for creating a private end point. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.private_network_info import PrivateNetworkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkInfo from a JSON string
private_network_info_instance = PrivateNetworkInfo.from_json(json)
# print the JSON string representation of the object
print(PrivateNetworkInfo.to_json())

# convert the object into a dict
private_network_info_dict = private_network_info_instance.to_dict()
# create an instance of PrivateNetworkInfo from a dict
private_network_info_from_dict = PrivateNetworkInfo.from_dict(private_network_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


