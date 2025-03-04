# CassandraSourceRegistrationPatchParams

Specifies parameters to update cassandra source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_credentials** | [**CassandraSourceRegistrationParamsAllOfCassandraCredentials**](CassandraSourceRegistrationParamsAllOfCassandraCredentials.md) |  | [optional] 
**commit_log_backup_location** | **str** | Commit Logs backup location on cassandra nodes | [optional] 
**config_directory** | **str** | Directory path containing Cassandra configuration YAML file. | [optional] 
**data_center_names** | **List[str]** | Data centers for this cluster. | [optional] 
**dse_configuration_directory** | **str** | Directory from where DSE specific configuration can be read. This should be set only when you are using the DSE distribution of Cassandra. | [optional] 
**dse_solr_info** | [**DSESolrInfo**](DSESolrInfo.md) |  | [optional] 
**is_dse_authenticator** | **bool** | Set to true if this cluster has DSE Authenticator. | [optional] 
**is_dse_tiered_storage** | **bool** | Set to true if this cluster has DSE tiered storage. | [optional] 
**jmx_credentials** | [**CassandraSourceRegistrationParamsAllOfJmxCredentials**](CassandraSourceRegistrationParamsAllOfJmxCredentials.md) |  | [optional] 
**kerberos_principal** | **str** | Principal for the kerberos connection. (This is required only if your Cassandra has Kerberos authentication. Please refer to the user guide.) | [optional] 
**seed_node** | **str** | Any one seed node of the Cassandra cluster. | [optional] 
**ssh_password_credentials** | [**SshPasswordCredentials**](SshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**SshPrivateKeyCredentials**](SshPrivateKeyCredentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.cassandra_source_registration_patch_params import CassandraSourceRegistrationPatchParams

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraSourceRegistrationPatchParams from a JSON string
cassandra_source_registration_patch_params_instance = CassandraSourceRegistrationPatchParams.from_json(json)
# print the JSON string representation of the object
print(CassandraSourceRegistrationPatchParams.to_json())

# convert the object into a dict
cassandra_source_registration_patch_params_dict = cassandra_source_registration_patch_params_instance.to_dict()
# create an instance of CassandraSourceRegistrationPatchParams from a dict
cassandra_source_registration_patch_params_from_dict = CassandraSourceRegistrationPatchParams.from_dict(cassandra_source_registration_patch_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


