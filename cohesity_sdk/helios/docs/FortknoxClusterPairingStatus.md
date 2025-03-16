# FortknoxClusterPairingStatus

Specifies the status of fortknox vault and cluster pairs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the message for corresponding status if there is any. | [optional] 
**status** | **str** | Specifies the status code. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_cluster_pairing_status import FortknoxClusterPairingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxClusterPairingStatus from a JSON string
fortknox_cluster_pairing_status_instance = FortknoxClusterPairingStatus.from_json(json)
# print the JSON string representation of the object
print(FortknoxClusterPairingStatus.to_json())

# convert the object into a dict
fortknox_cluster_pairing_status_dict = fortknox_cluster_pairing_status_instance.to_dict()
# create an instance of FortknoxClusterPairingStatus from a dict
fortknox_cluster_pairing_status_from_dict = FortknoxClusterPairingStatus.from_dict(fortknox_cluster_pairing_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


