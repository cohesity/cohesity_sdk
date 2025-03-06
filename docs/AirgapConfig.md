# AirgapConfig

Specifies the Airgap configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airgap_status** | **str** | Specifies Airgap should be enabled or disabled. | [optional] 
**exception_profiles** | **List[str]** | Specifies the firewall profiles allowed when Airgap is enabled. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.airgap_config import AirgapConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AirgapConfig from a JSON string
airgap_config_instance = AirgapConfig.from_json(json)
# print the JSON string representation of the object
print(AirgapConfig.to_json())

# convert the object into a dict
airgap_config_dict = airgap_config_instance.to_dict()
# create an instance of AirgapConfig from a dict
airgap_config_from_dict = AirgapConfig.from_dict(airgap_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


