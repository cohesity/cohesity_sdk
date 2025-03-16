# FortknoxClusterPairingInfo

Fortknox vault cluster pairing info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | The id of the paired cluster. | [optional] 
**cluster_incarnation_id** | **int** | The incarnation id of the paired cluster. | [optional] 
**pairing_status** | [**FortknoxClusterPairingStatus**](FortknoxClusterPairingStatus.md) |  | [optional] 
**vault_id** | **int** | The local vault id on the cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_cluster_pairing_info import FortknoxClusterPairingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxClusterPairingInfo from a JSON string
fortknox_cluster_pairing_info_instance = FortknoxClusterPairingInfo.from_json(json)
# print the JSON string representation of the object
print(FortknoxClusterPairingInfo.to_json())

# convert the object into a dict
fortknox_cluster_pairing_info_dict = fortknox_cluster_pairing_info_instance.to_dict()
# create an instance of FortknoxClusterPairingInfo from a dict
fortknox_cluster_pairing_info_from_dict = FortknoxClusterPairingInfo.from_dict(fortknox_cluster_pairing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


