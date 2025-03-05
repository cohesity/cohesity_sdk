# CouchbaseSourceRegistrationParams

Specifies parameters to register Couchbase source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**carrier_port** | **int** | Carrier direct or Carrier SSL port. | 
**http_port** | **int** | HTTP direct or HTTP SSL port. | 
**is_ssl_required** | **bool** | Set to true if connection to couchbase has to be using SSL. | 
**seeds** | **List[str]** | Specifies the IP Addresses or hostnames of the Couchbase cluster seed nodes. | 

## Example

```python
from cohesity_sdk.models.couchbase_source_registration_params import CouchbaseSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of CouchbaseSourceRegistrationParams from a JSON string
couchbase_source_registration_params_instance = CouchbaseSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(CouchbaseSourceRegistrationParams.to_json())

# convert the object into a dict
couchbase_source_registration_params_dict = couchbase_source_registration_params_instance.to_dict()
# create an instance of CouchbaseSourceRegistrationParams from a dict
couchbase_source_registration_params_from_dict = CouchbaseSourceRegistrationParams.from_dict(couchbase_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


