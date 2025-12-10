# ServiceAccountAttachedParams

Specifies the service account authentication method parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_email_address** | **str** | Specifies the client email address of the external target. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_account_attached_params import ServiceAccountAttachedParams

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountAttachedParams from a JSON string
service_account_attached_params_instance = ServiceAccountAttachedParams.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountAttachedParams.to_json())

# convert the object into a dict
service_account_attached_params_dict = service_account_attached_params_instance.to_dict()
# create an instance of ServiceAccountAttachedParams from a dict
service_account_attached_params_from_dict = ServiceAccountAttachedParams.from_dict(service_account_attached_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


