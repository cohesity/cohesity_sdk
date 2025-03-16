# HeliosCdpRetention

Specifies the retention of a CDP backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_lock_config** | [**DataLockConfig**](DataLockConfig.md) |  | [optional] 
**duration** | **int** | Specifies the duration for a cdp backup retention. | [optional] 
**unit** | **str** | Specificies the Retention Unit of a CDP backup measured in minutes or hours. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_cdp_retention import HeliosCdpRetention

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosCdpRetention from a JSON string
helios_cdp_retention_instance = HeliosCdpRetention.from_json(json)
# print the JSON string representation of the object
print(HeliosCdpRetention.to_json())

# convert the object into a dict
helios_cdp_retention_dict = helios_cdp_retention_instance.to_dict()
# create an instance of HeliosCdpRetention from a dict
helios_cdp_retention_from_dict = HeliosCdpRetention.from_dict(helios_cdp_retention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


