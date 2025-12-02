# WormConfig

Specifies WORM related configs for a LSU. Once enabled, WORM cannot be removed. Any view created on this LSU will inherit these configs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_retention_secs** | **int** | Specifies max retention period in seconds. It must be greater than or equal to &#x60;min_retention_secs&#x60;. | [optional] 
**min_retention_secs** | **int** | Specifies min retention period in seconds. It must be greater than 0. | [optional] 
**mode** | **str** | Specifies WORM mode. It can be set to either &#39;Enterprise&#39; or &#39;Compliance&#39;. If mode is set to &#39;Compliance&#39;, it cannot be changed later. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.worm_config import WormConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WormConfig from a JSON string
worm_config_instance = WormConfig.from_json(json)
# print the JSON string representation of the object
print(WormConfig.to_json())

# convert the object into a dict
worm_config_dict = worm_config_instance.to_dict()
# create an instance of WormConfig from a dict
worm_config_from_dict = WormConfig.from_dict(worm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


