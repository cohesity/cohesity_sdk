# EulaConfig

Specifies the End User License Agreement acceptance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_by_user** | **str** | Specifies the login account name for the Cohesity user who accepted the End User License Agreement. | [optional] 
**signed_time** | **int** | Specifies the time that the End User License Agreement was accepted. | [optional] 
**signed_version** | **int** | Specifies the version of the End User License Agreement that was accepted. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.eula_config import EulaConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EulaConfig from a JSON string
eula_config_instance = EulaConfig.from_json(json)
# print the JSON string representation of the object
print(EulaConfig.to_json())

# convert the object into a dict
eula_config_dict = eula_config_instance.to_dict()
# create an instance of EulaConfig from a dict
eula_config_from_dict = EulaConfig.from_dict(eula_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


