# VmwareSQLCredentialParams

Specifies the credentials to connect to SQL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  password for when agent is not installed | [optional] 
**username** | **str** |  username for when agent is not installed | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vmware_sql_credential_params import VmwareSQLCredentialParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareSQLCredentialParams from a JSON string
vmware_sql_credential_params_instance = VmwareSQLCredentialParams.from_json(json)
# print the JSON string representation of the object
print(VmwareSQLCredentialParams.to_json())

# convert the object into a dict
vmware_sql_credential_params_dict = vmware_sql_credential_params_instance.to_dict()
# create an instance of VmwareSQLCredentialParams from a dict
vmware_sql_credential_params_from_dict = VmwareSQLCredentialParams.from_dict(vmware_sql_credential_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


