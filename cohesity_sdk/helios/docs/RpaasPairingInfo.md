# RpaasPairingInfo

Holds the RPaaS Vault Information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Cluster ID configured for the region. | [optional] 
**cluster_incarnation_id** | **int** | Cluster Incarnation ID configured for the region. | [optional] 
**pairing_status** | [**PairingStatus**](PairingStatus.md) |  | [optional] 
**vault_id** | **int** | Specifies the vault ID associated with the region. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.rpaas_pairing_info import RpaasPairingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RpaasPairingInfo from a JSON string
rpaas_pairing_info_instance = RpaasPairingInfo.from_json(json)
# print the JSON string representation of the object
print(RpaasPairingInfo.to_json())

# convert the object into a dict
rpaas_pairing_info_dict = rpaas_pairing_info_instance.to_dict()
# create an instance of RpaasPairingInfo from a dict
rpaas_pairing_info_from_dict = RpaasPairingInfo.from_dict(rpaas_pairing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


