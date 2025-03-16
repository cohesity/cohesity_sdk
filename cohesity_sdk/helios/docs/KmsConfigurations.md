# KmsConfigurations

Key management systems configured on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_management_systems** | [**List[KmsConfiguration]**](KmsConfiguration.md) | Key management systems configured on the cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.kms_configurations import KmsConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of KmsConfigurations from a JSON string
kms_configurations_instance = KmsConfigurations.from_json(json)
# print the JSON string representation of the object
print(KmsConfigurations.to_json())

# convert the object into a dict
kms_configurations_dict = kms_configurations_instance.to_dict()
# create an instance of KmsConfigurations from a dict
kms_configurations_from_dict = KmsConfigurations.from_dict(kms_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


