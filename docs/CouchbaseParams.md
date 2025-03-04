# CouchbaseParams

Specifies the recovery options specific to Couchbase environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_couchbase_params** | [**RecoverCouchbaseParams**](RecoverCouchbaseParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.models.couchbase_params import CouchbaseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CouchbaseParams from a JSON string
couchbase_params_instance = CouchbaseParams.from_json(json)
# print the JSON string representation of the object
print(CouchbaseParams.to_json())

# convert the object into a dict
couchbase_params_dict = couchbase_params_instance.to_dict()
# create an instance of CouchbaseParams from a dict
couchbase_params_from_dict = CouchbaseParams.from_dict(couchbase_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


