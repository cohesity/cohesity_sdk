# DB2SourceRegistrationParams

Specifies parameters to register a DB2 source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_os_type** | **str** | Specifies the type of DB2 host. | [optional] 
**hosts** | **List[str]** | Specifies the IPs/hostnames for the nodes forming the DB2 source cluster. | 
**profile_path** | **str** | Specifies file location of DB2 Profile path of the instance. | 
**script_dir** | **str** | Specifies the absolute path of scripts used to interact with the DB2 source. | 
**source_name** | **str** | Specifies user friendly unique name provided for registering DB2 source. | 
**source_registration_arguments** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the source registration scripts. | [optional] 
**username** | **str** | Specifies the username to access target DB2 entity. | 

## Example

```python
from cohesity_sdk.cluster.models.db2_source_registration_params import DB2SourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of DB2SourceRegistrationParams from a JSON string
db2_source_registration_params_instance = DB2SourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(DB2SourceRegistrationParams.to_json())

# convert the object into a dict
db2_source_registration_params_dict = db2_source_registration_params_instance.to_dict()
# create an instance of DB2SourceRegistrationParams from a dict
db2_source_registration_params_from_dict = DB2SourceRegistrationParams.from_dict(db2_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


