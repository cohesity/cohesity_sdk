# CdpRetention

Specifies the retention of a CDP backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_lock_config** | [**DataLockConfig**](DataLockConfig.md) |  | [optional] 
**duration** | **int** | Specifies the duration for a cdp backup retention. | 
**unit** | **str** | Specificies the Retention Unit of a CDP backup measured in minutes or hours. | 

## Example

```python
from cohesity_sdk.helios.models.cdp_retention import CdpRetention

# TODO update the JSON string below
json = "{}"
# create an instance of CdpRetention from a JSON string
cdp_retention_instance = CdpRetention.from_json(json)
# print the JSON string representation of the object
print(CdpRetention.to_json())

# convert the object into a dict
cdp_retention_dict = cdp_retention_instance.to_dict()
# create an instance of CdpRetention from a dict
cdp_retention_from_dict = CdpRetention.from_dict(cdp_retention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


