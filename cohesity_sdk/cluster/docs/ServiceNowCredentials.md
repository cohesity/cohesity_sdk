# ServiceNowCredentials

Specifies the credentials to register a ServiceNow source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password for basic credential authentication. | 
**username** | **str** | Specifies the username for basic credential authentication. | 

## Example

```python
from cohesity_sdk.cluster.models.service_now_credentials import ServiceNowCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNowCredentials from a JSON string
service_now_credentials_instance = ServiceNowCredentials.from_json(json)
# print the JSON string representation of the object
print(ServiceNowCredentials.to_json())

# convert the object into a dict
service_now_credentials_dict = service_now_credentials_instance.to_dict()
# create an instance of ServiceNowCredentials from a dict
service_now_credentials_from_dict = ServiceNowCredentials.from_dict(service_now_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


