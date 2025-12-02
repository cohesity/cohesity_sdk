# PostgresSourceRegistrationParams

Specifies parameters to register a Postgres source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**pg_bin** | **str** | Specifies the directory containing the PostgreSQL binaries. | [optional] 
**pg_host** | **str** | Specifies the host for the Postgres source. | [optional] 
**pg_port** | **int** | Specifies the port for the Postgres source. | 
**archive_mode** | **bool** | Specifies the archive mode for the Postgres source. | 
**check_db_connection** | **bool** | Specifies whether to check the database connection for the Postgres source. | 
**environment_variables** | **List[str]** | Specifies the environment variables for the Postgres source. | [optional] 
**hosts** | **List[str]** | Specifies the IPs/hostnames for the nodes forming the Postgres source cluster. | 
**kerberos_keytab** | **str** | Specifies the Kerberos keytab file for the Postgres source authentication. | [optional] 
**kerberos_principal** | **str** | Specifies the Kerberos principal for the Postgres source authentication. | [optional] 
**script_dir** | **str** | Specifies the directory containing the scripts used to interact with the Postgres source. | 
**source_name** | **str** | Specifies user friendly unique name provided for registering Postgres source. | 
**ssl_certificate_dir** | **str** | Specifies the directory containing the SSL certificates for the Postgres source authentication. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.postgres_source_registration_params import PostgresSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresSourceRegistrationParams from a JSON string
postgres_source_registration_params_instance = PostgresSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(PostgresSourceRegistrationParams.to_json())

# convert the object into a dict
postgres_source_registration_params_dict = postgres_source_registration_params_instance.to_dict()
# create an instance of PostgresSourceRegistrationParams from a dict
postgres_source_registration_params_from_dict = PostgresSourceRegistrationParams.from_dict(postgres_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


