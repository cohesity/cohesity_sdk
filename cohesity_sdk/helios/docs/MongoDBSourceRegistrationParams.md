# MongoDBSourceRegistrationParams

Specifies parameters to register MongoDB source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | MongoDB authentication type. | 
**authenticating_database** | **str** | Authenticating Database for this cluster. Should be set if &#39;authType&#39; is &#39;LDAP&#39; or &#39;SCRAM&#39;. | [optional] 
**hosts** | **List[str]** | Specify the MongoS hosts for a sharded cluster and the MongoD hosts for a non-sharded cluster. You can specify a sub-set of the hosts. | 
**is_ssl_required** | **bool** | Set to true if connection to MongoDB has to be over SSL. | 
**password** | **str** | Specifies the password for the MongoDB cluster. Should be set if &#39;authType&#39; is &#39;LDAP&#39; or &#39;SCRAM&#39;. | [optional] 
**principal** | **str** | Specifies the principal name of the MongoDB cluster. Should be set if &#39;authType&#39; is &#39;KERBEROS&#39;. | [optional] 
**secondary_node_tag** | **str** | MongoDB Secondary node tag. Required only if &#39;useSecondaryForBackup&#39; is true.The system will use this to identify the secondary nodes for reading backup data. | [optional] 
**use_secondary_for_backup** | **bool** | Set this to true if you want the system to peform backups from secondary nodes. | 
**username** | **str** | Specifies the username of the MongoDB cluster. Should be set if &#39;authType&#39; is &#39;LDAP&#39; or &#39;SCRAM&#39;. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mongo_db_source_registration_params import MongoDBSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBSourceRegistrationParams from a JSON string
mongo_db_source_registration_params_instance = MongoDBSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(MongoDBSourceRegistrationParams.to_json())

# convert the object into a dict
mongo_db_source_registration_params_dict = mongo_db_source_registration_params_instance.to_dict()
# create an instance of MongoDBSourceRegistrationParams from a dict
mongo_db_source_registration_params_from_dict = MongoDBSourceRegistrationParams.from_dict(mongo_db_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


