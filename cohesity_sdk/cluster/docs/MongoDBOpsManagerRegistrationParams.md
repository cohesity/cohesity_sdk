# MongoDBOpsManagerRegistrationParams

Specifies parameters to register MongoDB Ops Manager.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificate** | **str** | Specifies the CA certificate to enable SSL communication with Ops manager. | [optional] 
**hostname** | **str** | Specify the MongoDB Ops Manager hostname or IP address. | 
**is_ssl_required** | **bool** | Set to true if connection to MongoDB has to be over SSL. | 
**port** | **int** | Specifies port for the connection. | 
**private_key** | **str** | Specifies the private key for connection. | 
**public_key** | **str** | Specifies the public key for connection. | 

## Example

```python
from cohesity_sdk.cluster.models.mongo_db_ops_manager_registration_params import MongoDBOpsManagerRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBOpsManagerRegistrationParams from a JSON string
mongo_db_ops_manager_registration_params_instance = MongoDBOpsManagerRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(MongoDBOpsManagerRegistrationParams.to_json())

# convert the object into a dict
mongo_db_ops_manager_registration_params_dict = mongo_db_ops_manager_registration_params_instance.to_dict()
# create an instance of MongoDBOpsManagerRegistrationParams from a dict
mongo_db_ops_manager_registration_params_from_dict = MongoDBOpsManagerRegistrationParams.from_dict(mongo_db_ops_manager_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


