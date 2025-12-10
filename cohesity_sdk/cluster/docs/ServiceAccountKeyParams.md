# ServiceAccountKeyParams

Specifies the API key authentication method parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_email_address** | **str** | Specifies the client email address of the external target. | [optional] 
**client_private_key** | **str** | Specifies the client private key of the external target. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_account_key_params import ServiceAccountKeyParams

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountKeyParams from a JSON string
service_account_key_params_instance = ServiceAccountKeyParams.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountKeyParams.to_json())

# convert the object into a dict
service_account_key_params_dict = service_account_key_params_instance.to_dict()
# create an instance of ServiceAccountKeyParams from a dict
service_account_key_params_from_dict = ServiceAccountKeyParams.from_dict(service_account_key_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


