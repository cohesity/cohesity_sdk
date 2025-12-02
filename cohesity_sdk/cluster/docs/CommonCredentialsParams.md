# CommonCredentialsParams

Specifies the common params of credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password for Cohesity user to use when connecting to the cluster. | 
**username** | **str** | Specifies the Cohesity user name used to connect to the cluster. | 

## Example

```python
from cohesity_sdk.cluster.models.common_credentials_params import CommonCredentialsParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonCredentialsParams from a JSON string
common_credentials_params_instance = CommonCredentialsParams.from_json(json)
# print the JSON string representation of the object
print(CommonCredentialsParams.to_json())

# convert the object into a dict
common_credentials_params_dict = common_credentials_params_instance.to_dict()
# create an instance of CommonCredentialsParams from a dict
common_credentials_params_from_dict = CommonCredentialsParams.from_dict(common_credentials_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


